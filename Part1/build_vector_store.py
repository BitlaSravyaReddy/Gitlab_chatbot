from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

# Load content
handbook_text = Path("Part1/data/handbook_cleaned_FULL.txt").read_text(encoding="utf-8")
direction_text = Path("Part1/data/direction_final.txt").read_text(encoding="utf-8")


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
handbook_docs = chunk_with_metadata(handbook_text, "handbook")
direction_docs = chunk_with_metadata(direction_text, "direction")
all_docs = handbook_docs + direction_docs
print(f"✅ Total chunks: {len(all_docs)}")


# Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# Vector store
vectordb = FAISS.from_documents(all_docs, embedding_model)
vectordb.save_local("Part1/data/faiss_index")
print("✅ FAISS index saved to: Part1/data/faiss_index/")