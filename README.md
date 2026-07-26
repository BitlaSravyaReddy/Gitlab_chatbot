# 🦊 GitLab AI Chatbot

> An AI-powered assistant that answers questions about GitLab's Handbook and product Direction — grounded in retrieved sources, powered by Pinecone DB and Google Gemini 2.5 Flash.

---

## ✨ Features

- 🔍 **Semantic Search** — Retrieves the most relevant handbook/direction sections using Pinecone vector DB
- 🤖 **Gemini 2.5 Flash** — Generates accurate, context-aware answers from retrieved sources
- 💬 **Conversational Memory** — Remembers the chat history for follow-up questions
- 📚 **Source Citations** — Every answer comes with the exact source sections used
- ⚡ **Unified Deployment** — FastAPI backend serves the React frontend from a single server
- 🎨 **Apple Luxury UI** — Clean, minimal React interface with Inter typography and Apple-blue accents
- ☁️ **Render-ready** — One-click deploy via `render.yaml`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      RENDER DEPLOYMENT                       │
│                                                             │
│  ┌──────────────┐   Build   ┌───────────────────────────┐  │
│  │ React Frontend│ ───────▶ │       FastAPI Backend      │  │
│  │  (TanStack   │           │   serves /  + /chat        │  │
│  │   Start+Vite)│           │   + /health + /docs        │  │
│  └──────────────┘           └─────────────┬──────────────┘  │
│                                           │                  │
└───────────────────────────────────────────│──────────────────┘
                                            │ LangChain QA Chain
                              ┌─────────────┴──────────────┐
                              │                            │
                    ┌─────────▼────────┐       ┌──────────▼──────────┐
                    │   Pinecone DB    │       │  Gemini 2.5 Flash   │
                    │  (gitlab-chatbot │       │   (Google AI API)   │
                    │   384-dim cosine)│       └─────────────────────┘
                    └──────────────────┘
```

**Full architecture diagram** → see [`architecture.md`](architecture.md) *(generated separately)*

---

## 📁 Project Structure

```
Gitlab_chatbot/
├── Part1/                          # 🗂️ Data ingestion & vector store builder
│   ├── build_vector_store.py       #    Chunks docs, embeds & uploads to Pinecone
│   └── data/
│       ├── handbook_final.txt      #    GitLab Handbook source
│       ├── direction_final.txt     #    GitLab Direction source
│       └── faiss_index/            #    Local FAISS fallback (auto-generated)
│
├── Part2/                          # 🤖 LLM & retrieval chain
│   ├── llm_integration.py          #    Pinecone retriever + Gemini QA chain
│   └── .env                        #    Optional: Part2-specific env overrides
│
├── Part3/                          # 🌐 Streamlit UI (standalone mode)
│   └── streamlit.py
│
├── gitlab-insight-bot-main/        # 🖥️ React frontend (Apple luxury UI)
│   ├── src/
│   │   ├── routes/index.tsx        #    Main chat page
│   │   ├── styles.css              #    Apple design system (oklch palette)
│   │   └── lib/chat-api.ts         #    Auto-detecting API client
│   └── package.json
│
├── api.py                          # ⚙️ FastAPI backend (unified server)
├── render.yaml                     # ☁️ Render.com deployment spec
├── requirements.txt                # 🐍 Python dependencies
└── .env                            # 🔐 API keys (never commit this!)
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- A [Pinecone](https://pinecone.io) account + API key
- A [Google AI Studio](https://aistudio.google.com) Gemini API key

### 1. Clone & Install

```bash
git clone <your-repo-url>
cd Gitlab_chatbot

# Python deps
pip install -r requirements.txt

# Frontend deps
cd gitlab-insight-bot-main
npm install --legacy-peer-deps
npm run build
cd ..
```

### 2. Configure Environment

Create a `.env` file in the project root:

```env
# Google Gemini
GOOGLE_API_KEY=your_gemini_api_key_here

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=gitlab-chatbot
```

### 3. Build the Vector Store (first time only)

```bash
python Part1/build_vector_store.py
```

This will:
- Read the handbook & direction text files
- Chunk them into 512-token segments
- Generate `all-MiniLM-L6-v2` embeddings (384-dim)
- Upload all chunks to your Pinecone index `gitlab-chatbot`
- Save a local FAISS fallback index to `Part1/data/faiss_index/`

### 4. Run the App

```bash
# Start the unified FastAPI + React server
python api.py
```

Open **[http://localhost:8000](http://localhost:8000)** — the React UI is served directly by FastAPI.

> **Swagger API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🖥️ Development Mode (Hot Reload)

Run the backend and frontend dev servers separately:

```bash
# Terminal 1 — FastAPI backend
python api.py

# Terminal 2 — Vite dev server (hot reload)
cd gitlab-insight-bot-main
npm run dev
```

Open the Vite dev URL (e.g. `http://localhost:8080`). The frontend automatically routes API calls to `http://127.0.0.1:8000`.

---

## ☁️ Deploy to Render

1. Push this repository to GitHub / GitLab
2. Create a new **Web Service** on [Render.com](https://render.com)
3. Connect your repository — Render will auto-detect `render.yaml`
4. Add Environment Variables in the Render dashboard:
   - `GOOGLE_API_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_INDEX_NAME` → `gitlab-chatbot`
5. Click **Deploy**

The `render.yaml` build command:
```bash
pip install -r requirements.txt && cd gitlab-insight-bot-main && npm install --legacy-peer-deps && npm run build
```

Start command:
```bash
uvicorn api:app --host 0.0.0.0 --port $PORT
```

---

## 🔌 API Reference

### `GET /health`
Returns the status of the backend and Pinecone connection.

```json
{
  "status": "healthy",
  "vector_db": "Pinecone DB",
  "pinecone_index": "gitlab-chatbot"
}
```

### `POST /chat`
Ask the AI assistant a question.

**Request:**
```json
{
  "question": "What are GitLab's core values?"
}
```

**Response:**
```json
{
  "answer": "GitLab's core values are...",
  "sources": [
    {
      "source": "handbook_final.txt",
      "section": "Values",
      "snippet": "Our values are CREDIT: Collaboration, Results, Efficiency..."
    }
  ]
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React · TanStack Start · Vite · TypeScript · Tailwind CSS |
| **Backend** | FastAPI · Uvicorn · Python 3.12 |
| **LLM** | Google Gemini 2.5 Flash (`langchain-google-genai`) |
| **Embeddings** | `all-MiniLM-L6-v2` via HuggingFace (384-dim) |
| **Vector DB** | Pinecone Serverless (cosine similarity) |
| **Fallback DB** | FAISS (local, offline) |
| **Orchestration** | LangChain · ConversationalRetrievalChain |
| **Memory** | ConversationSummaryBufferMemory |
| **Deployment** | Render.com |
| **Standalone UI** | Streamlit (Part3) |

---

## 🔐 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GOOGLE_API_KEY` | ✅ | Google AI Studio / Gemini API key |
| `PINECONE_API_KEY` | ✅ | Pinecone API key |
| `PINECONE_INDEX_NAME` | ✅ | Pinecone index name (default: `gitlab-chatbot`) |
| `VITE_API_BASE_URL` | ⬜ | Override frontend API URL (e.g. for custom domains) |

> ⚠️ Never commit your `.env` file. It is already in `.gitignore`.

---

## 🙏 Data Sources

- [GitLab Handbook](https://handbook.gitlab.com) — company culture, processes, values
- [GitLab Direction](https://about.gitlab.com/direction/) — product strategy and roadmap

---

## 📄 License

MIT
