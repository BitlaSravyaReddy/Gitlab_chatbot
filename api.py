import os
import sys
from pathlib import Path
from contextlib import asynccontextmanager
from typing import List, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# Ensure parent directory is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# Load .env files
load_dotenv(dotenv_path=BASE_DIR / ".env")
load_dotenv(dotenv_path=BASE_DIR / "Part2" / ".env")

from Part2.llm_integration import build_qa_chain

# Global QA Chain holder
qa_chain = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler to pre-initialize vector store and LLM chain on app startup."""
    global qa_chain
    print("🌲 Initializing Pinecone DB & Gemini QA Chain for FastAPI...")
    try:
        qa_chain = build_qa_chain()
        print("✅ QA Chain successfully loaded and ready for API requests!")
    except Exception as e:
        print(f"⚠️ Warning: Error initializing QA chain during startup: {e}")
    yield
    print("👋 Shutting down FastAPI application...")

# Initialize FastAPI App
app = FastAPI(
    title="GitLab AI Chatbot API",
    description="FastAPI Backend for GitLab Handbook & Direction AI Chatbot powered by Pinecone DB & Gemini",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Locate static build output from frontend if available
FRONTEND_BUILD_DIRS = [
    BASE_DIR / "gitlab-insight-bot-main" / "dist",
    BASE_DIR / "gitlab-insight-bot-main" / ".output" / "public",
    BASE_DIR / "dist",
]

FRONTEND_STATIC_DIR = None
for candidate in FRONTEND_BUILD_DIRS:
    if candidate.exists() and candidate.is_dir():
        FRONTEND_STATIC_DIR = candidate
        break

if FRONTEND_STATIC_DIR:
    print(f"🎨 Serving frontend assets from: {FRONTEND_STATIC_DIR}")
    assets_dir = FRONTEND_STATIC_DIR / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

# --- Pydantic Schemas ---
class ChatRequest(BaseModel):
    question: str = Field(..., example="What are GitLab's core values?", description="User query for the chatbot")

class SourceDocument(BaseModel):
    source: str = Field(..., description="Document source name (e.g. handbook or direction)")
    section: str = Field(..., description="Section title or header")
    snippet: str = Field(..., description="Retrieved content snippet")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="Generated AI response")
    sources: List[SourceDocument] = Field(default_factory=list, description="Source documents retrieved from Pinecone DB")

class HealthStatus(BaseModel):
    status: str
    vector_db: str
    pinecone_index: str

# --- Endpoints ---
@app.get("/health", response_model=HealthStatus, tags=["General"])
async def health_check():
    index_name = os.getenv("PINECONE_INDEX_NAME", "gitlab-chatbot")
    return HealthStatus(
        status="healthy" if qa_chain is not None else "degraded",
        vector_db="Pinecone DB",
        pinecone_index=index_name
    )

@app.post("/chat", response_model=ChatResponse, tags=["Chatbot"])
async def chat(request: ChatRequest):
    global qa_chain
    if qa_chain is None:
        try:
            qa_chain = build_qa_chain()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"QA Chain unavailable: {str(e)}")

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question parameter cannot be empty.")

    try:
        result = qa_chain.invoke({"question": request.question})
        answer = result.get("answer", "")
        raw_sources = result.get("source_documents", [])

        sources = []
        for doc in raw_sources:
            meta = getattr(doc, "metadata", {})
            sources.append(
                SourceDocument(
                    source=meta.get("source", "Unknown"),
                    section=meta.get("section", "N/A"),
                    snippet=doc.page_content.strip()[:500] + "..." if len(doc.page_content) > 500 else doc.page_content.strip()
                )
            )

        return ChatResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@app.get("/api/info", tags=["General"])
async def api_info():
    return {
        "message": "GitLab AI Chatbot API is online 🚀",
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc"
    }

@app.get("/", tags=["General"])
async def serve_root():
    if FRONTEND_STATIC_DIR:
        index_file = FRONTEND_STATIC_DIR / "index.html"
        if index_file.exists():
            return FileResponse(str(index_file))
    return {
        "message": "GitLab AI Chatbot API is online 🚀",
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
