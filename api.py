import os
import sys
import subprocess
import signal
import atexit
from pathlib import Path
from contextlib import asynccontextmanager
from typing import List

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel, Field

# ─── Path setup ───────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

load_dotenv(dotenv_path=BASE_DIR / ".env")
load_dotenv(dotenv_path=BASE_DIR / "Part2" / ".env")

from Part2.llm_integration import build_qa_chain

# ─── Frontend config ──────────────────────────────────────────────────────────
FRONTEND_DIR = BASE_DIR / "gitlab-insight-bot-main"
NITRO_SERVER_ENTRY = FRONTEND_DIR / ".output" / "server" / "index.mjs"
PUBLIC_DIR = FRONTEND_DIR / ".output" / "public"

# Port the Nitro SSR server will listen on internally
NITRO_PORT = 3111
_nitro_process: subprocess.Popen | None = None

def _start_nitro():
    """Start the Nitro SSR server as a background subprocess."""
    global _nitro_process
    if not NITRO_SERVER_ENTRY.exists():
        print(f"⚠️  Nitro server entry not found at {NITRO_SERVER_ENTRY}")
        print("   Run: cd gitlab-insight-bot-main && npm run build")
        return

    env = {**os.environ, "PORT": str(NITRO_PORT), "HOST": "127.0.0.1"}
    _nitro_process = subprocess.Popen(
        ["node", str(NITRO_SERVER_ENTRY)],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(f"🖥️  Nitro SSR server started (PID {_nitro_process.pid}) on port {NITRO_PORT}")

def _stop_nitro():
    """Terminate the Nitro subprocess on FastAPI shutdown."""
    global _nitro_process
    if _nitro_process and _nitro_process.poll() is None:
        print(f"🛑 Stopping Nitro server (PID {_nitro_process.pid})...")
        _nitro_process.send_signal(signal.SIGTERM)
        try:
            _nitro_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            _nitro_process.kill()

atexit.register(_stop_nitro)

# ─── QA Chain ─────────────────────────────────────────────────────────────────
qa_chain = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global qa_chain

    # Start Nitro SSR server
    _start_nitro()

    # Pre-load QA chain
    print("🌲 Initializing Pinecone DB & Gemini QA Chain...")
    try:
        qa_chain = build_qa_chain()
        print("✅ QA Chain ready!")
    except Exception as e:
        print(f"⚠️  QA chain init failed: {e}")

    yield
    _stop_nitro()
    print("👋 Shutdown complete.")

# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="GitLab AI Chatbot API",
    description="FastAPI backend for GitLab Handbook & Direction AI — Pinecone DB + Gemini 2.5 Flash",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static assets (JS/CSS) served directly by FastAPI for performance
if PUBLIC_DIR.is_dir():
    assets_dir = PUBLIC_DIR / "assets"
    if assets_dir.is_dir():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")
    print(f"🎨 Static assets mounted from {PUBLIC_DIR}")

# ─── Pydantic schemas ─────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str = Field(..., example="What are GitLab's core values?")

class SourceDocument(BaseModel):
    source: str
    section: str
    snippet: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceDocument] = []

class HealthStatus(BaseModel):
    status: str
    vector_db: str
    pinecone_index: str

# ─── API routes ───────────────────────────────────────────────────────────────
@app.get("/health", response_model=HealthStatus, tags=["General"])
async def health_check():
    return HealthStatus(
        status="healthy" if qa_chain is not None else "degraded",
        vector_db="Pinecone DB",
        pinecone_index=os.getenv("PINECONE_INDEX_NAME", "gitlab-chatbot"),
    )

@app.get("/api/info", tags=["General"])
async def api_info():
    return {"message": "GitLab AI Chatbot API is online 🚀", "docs": "/api/docs"}

@app.post("/chat", response_model=ChatResponse, tags=["Chatbot"])
async def chat(request: ChatRequest):
    global qa_chain
    if qa_chain is None:
        try:
            qa_chain = build_qa_chain()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"QA Chain unavailable: {e}")

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    try:
        result = qa_chain.invoke({"question": request.question})
        answer = result.get("answer", "")
        sources = []
        for doc in result.get("source_documents", []):
            meta = getattr(doc, "metadata", {})
            content = doc.page_content.strip()
            sources.append(SourceDocument(
                source=meta.get("source", "Unknown"),
                section=meta.get("section", "N/A"),
                snippet=content[:500] + "..." if len(content) > 500 else content,
            ))
        return ChatResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# ─── Favicon ──────────────────────────────────────────────────────────────────
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    fav = PUBLIC_DIR / "favicon.ico"
    if fav.exists():
        return FileResponse(str(fav))
    raise HTTPException(status_code=404)

# ─── SPA/SSR proxy catch-all ──────────────────────────────────────────────────
# All non-API requests are proxied to the Nitro SSR server which renders the React app.
@app.api_route("/{full_path:path}", methods=["GET", "HEAD"], include_in_schema=False)
async def proxy_to_nitro(full_path: str, request: Request):
    # Skip — already handled above
    if full_path.startswith(("api/", "chat", "health", "assets/")):
        raise HTTPException(status_code=404)

    if _nitro_process is None or _nitro_process.poll() is not None:
        return JSONResponse(
            status_code=503,
            content={
                "error": "Frontend server not running",
                "hint": "Run: cd gitlab-insight-bot-main && npm run build, then restart.",
                "api_docs": "/api/docs",
            },
        )

    nitro_url = f"http://127.0.0.1:{NITRO_PORT}/{full_path}"
    if request.url.query:
        nitro_url += f"?{request.url.query}"

    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            resp = await client.request(
                method=request.method,
                url=nitro_url,
                headers={k: v for k, v in request.headers.items() if k.lower() != "host"},
            )
            return Response(
                content=resp.content,
                status_code=resp.status_code,
                headers=dict(resp.headers),
                media_type=resp.headers.get("content-type", "text/html"),
            )
        except httpx.ConnectError:
            return JSONResponse(
                status_code=503,
                content={"error": "Frontend SSR server not reachable. It may still be starting up."},
            )

# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=9000, reload=False)
