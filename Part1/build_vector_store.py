import os
import time
from pathlib import Path
from dotenv import load_dotenv

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
try:
    from langchain_huggingface import HuggingFaceEmbeddings
except Exception:
    from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
root_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=root_env)
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") or os.getenv("PINECONE_DB")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "gitlab-chatbot")

if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY or PINECONE_DB is missing from environment variables!")

# Base directory setup
BASE_DIR = Path(__file__).resolve().parent

# Load content
handbook_path = BASE_DIR / "data" / "handbook_cleaned_FULL.txt"
direction_path = BASE_DIR / "data" / "direction_final.txt"

print(f"📖 Reading source data files from {BASE_DIR / 'data'}...")
handbook_text = handbook_path.read_text(encoding="utf-8")
direction_text = direction_path.read_text(encoding="utf-8")

# Initialize text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=150,
    length_function=len,
)

def chunk_with_metadata(text: str, source_label: str):
    """Split text into chunks with metadata."""
    sections = text.split("## SECTION:")
    documents = []

    for section in sections:
        if not section.strip():
            continue
        header, *content = section.strip().split("\n", 1)
        body = content[0] if content else ""
        chunks = splitter.create_documents([body])
        for chunk in chunks:
            chunk.metadata = {
                "source": source_label,
                "section": header.strip()
            }
        documents.extend(chunks)
    return documents

# Chunk text
print("✂️ Chunking documents...")
handbook_docs = chunk_with_metadata(handbook_text, "handbook")
direction_docs = chunk_with_metadata(direction_text, "direction")
all_docs = handbook_docs + direction_docs
print(f"✅ Total chunks created: {len(all_docs)}")

# Embedding Model (384 dimensions)
print("🧠 Initializing HuggingFace Embeddings (all-MiniLM-L6-v2)...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Pinecone Setup & Indexing
print(f"🌲 Connecting to Pinecone DB (Index: '{INDEX_NAME}')...")
pc = Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [idx.name for idx in pc.list_indexes()]

if INDEX_NAME not in existing_indexes:
    print(f"⚙️ Index '{INDEX_NAME}' not found. Creating new Pinecone index (dimension=384, metric='cosine')...")
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print("⏳ Waiting for index to be ready...")
    while not pc.describe_index(INDEX_NAME).status['ready']:
        time.sleep(1)
    print(f"✅ Index '{INDEX_NAME}' is ready!")
else:
    print(f"✅ Found existing index '{INDEX_NAME}'.")

print(f"🚀 Uploading {len(all_docs)} document chunks to Pinecone DB in batches...")
# Batch upload to Pinecone to handle large document sets smoothly
batch_size = 100
for i in range(0, len(all_docs), batch_size):
    batch = all_docs[i:i + batch_size]
    print(f"   -> Uploading batch {i // batch_size + 1}/{(len(all_docs) - 1) // batch_size + 1} ({len(batch)} chunks)...")
    if i == 0:
        vectorstore = PineconeVectorStore.from_documents(
            documents=batch,
            embedding=embedding_model,
            index_name=INDEX_NAME
        )
    else:
        vectorstore.add_documents(documents=batch)

print("🎉 Successfully indexed all data to Pinecone DB!")

# Save local FAISS backup as well
print("💾 Saving local FAISS backup...")
faiss_dir = BASE_DIR / "data" / "faiss_index"
vectordb_faiss = FAISS.from_documents(all_docs, embedding_model)
vectordb_faiss.save_local(str(faiss_dir))
print(f"✅ Local FAISS index saved to: {faiss_dir}")