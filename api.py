import os
import sys
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ─── Path & Env setup ─────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

load_dotenv(dotenv_path=BASE_DIR / ".env")
load_dotenv(dotenv_path=BASE_DIR / "Part2" / ".env")

from Part2.llm_integration import build_qa_chain

# Global lazy holder for QA Chain
qa_chain = None

def get_qa_chain():
    """Lazily initialize the QA Chain on first demand instead of server startup."""
    global qa_chain
    if qa_chain is None:
        print("🌲 Lazily initializing Pinecone DB & Gemini QA Chain...")
        qa_chain = build_qa_chain()
        print("✅ QA Chain ready!")
    return qa_chain

# ─── FastAPI App ──────────────────────────────────────────────────────────────
app = FastAPI(
    title="GitLab AI Chatbot Backend API",
    description="FastAPI Backend for GitLab Handbook & Direction AI Chatbot powered by Pinecone DB & Gemini 2.5 Flash",
    version="1.0.0",
)

# Enable CORS for cross-origin requests (e.g. from separated React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Pydantic Schemas ─────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str = Field(..., example="What are GitLab's core values?", description="User query for the chatbot")

class SourceDocument(BaseModel):
    source: str = Field(..., description="Document source name")
    section: str = Field(..., description="Section title or header")
    snippet: str = Field(..., description="Retrieved content snippet")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="Generated AI response")
    sources: List[SourceDocument] = Field(default_factory=list, description="Source documents retrieved from Pinecone DB")

class HealthStatus(BaseModel):
    status: str
    vector_db: str
    pinecone_index: str

# ─── Endpoints ────────────────────────────────────────────────────────────────
@app.get("/", tags=["General"])
async def root():
    return {
        "message": "GitLab AI Chatbot API is online 🚀",
        "docs": "/docs",
        "health": "/health",
    }

@app.get("/health", response_model=HealthStatus, tags=["General"])
async def health_check():
    index_name = os.getenv("PINECONE_INDEX_NAME", "gitlab-chatbot")
    return HealthStatus(
        status="healthy",
        vector_db="Pinecone DB",
        pinecone_index=index_name,
    )

@app.get("/api/info", tags=["General"])
async def api_info():
    return {
        "message": "GitLab AI Chatbot API is online 🚀",
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc",
    }

@app.post("/chat", response_model=ChatResponse, tags=["Chatbot"])
async def chat(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question parameter cannot be empty.")

    try:
        chain = get_qa_chain()
        result = chain.invoke({"question": request.question})
        answer = result.get("answer", "")
        raw_sources = result.get("source_documents", [])

        sources = []
        for doc in raw_sources:
            meta = getattr(doc, "metadata", {})
            content = doc.page_content.strip()
            sources.append(
                SourceDocument(
                    source=meta.get("source", "Unknown"),
                    section=meta.get("section", "N/A"),
                    snippet=content[:500] + "..." if len(content) > 500 else content,
                )
            )

        return ChatResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

# ─── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
