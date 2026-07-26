# llm_integration.py
import os
import getpass
import warnings
from pathlib import Path
from dotenv import load_dotenv

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except Exception:
    from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS

try:
    from langchain.memory import ConversationSummaryBufferMemory
except ImportError:
    try:
        from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
    except ImportError:
        from langchain_community.memory.summary_buffer import ConversationSummaryBufferMemory

try:
    from langchain.chains import ConversationalRetrievalChain
except ImportError:
    try:
        from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
    except ImportError:
        from langchain_community.chains import ConversationalRetrievalChain

from langchain_google_genai import ChatGoogleGenerativeAI

try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate

warnings.filterwarnings("ignore", category=UserWarning, module="langchain_google_genai")

# Load .env variables from root or current directory
root_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=root_env)
load_dotenv()


# 🔐 API Key Setup
def setup_api_key(google_api_key: str = None, pinecone_api_key: str = None):
    if google_api_key:
        os.environ["GOOGLE_API_KEY"] = google_api_key
    if pinecone_api_key:
        os.environ["PINECONE_API_KEY"] = pinecone_api_key


# 🧠 Load Pinecone Vector DB (with FAISS local fallback) & Retriever
def load_vector_store(index_name: str = None):
    index_name = index_name or os.getenv("PINECONE_INDEX_NAME", "gitlab-chatbot")
    pinecone_api_key = os.getenv("PINECONE_API_KEY") or os.getenv("PINECONE_DB")
    
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if pinecone_api_key:
        os.environ["PINECONE_API_KEY"] = pinecone_api_key
        try:
            print(f"🌲 Connecting to Pinecone DB index '{index_name}'...")
            vectordb = PineconeVectorStore.from_existing_index(
                index_name=index_name,
                embedding=embedding
            )
            return vectordb.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 8, "fetch_k": 18}
            )
        except Exception as e:
            print(f"⚠️ Could not load Pinecone index ('{e}'). Falling back to local FAISS index...")
    else:
        print("⚠️ No Pinecone API key found. Using local FAISS index...")

    # Local FAISS Fallback
    base_dir = Path(__file__).resolve().parent.parent
    faiss_path = base_dir / "Part1" / "data" / "faiss_index"
    
    if not faiss_path.exists():
        raise FileNotFoundError(f"❌ Neither Pinecone DB nor local FAISS index ({faiss_path}) is available.")

    vectordb = FAISS.load_local(
        str(faiss_path),
        embedding,
        allow_dangerous_deserialization=True
    )
    return vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 8, "fetch_k": 18}
    )


# 🤖 Build QA Chain
def build_qa_chain():
    retriever = load_vector_store()
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        convert_system_message_to_human=True,
    )

    memory = ConversationSummaryBufferMemory(
        llm=gemini_llm,
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an expert assistant trained on GitLab's official Handbook and Direction documents.

Please:
- Answer with as much useful detail as possible.
- Use bullet points or formatting if appropriate.
- Cite the source section when available.
- Only answer from GitLab materials. Politely decline anything off-topic.

Context:
{context}

Question:
{question}"""
    )

    return ConversationalRetrievalChain.from_llm(
        llm=gemini_llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt},
        output_key="answer",
        verbose=False
    )


# 🚀 Terminal entry point
if __name__ == "__main__":
    g_key = os.getenv("GOOGLE_API_KEY")
    if not g_key:
        g_key = getpass.getpass("Enter your Google API Key: ")
        os.environ["GOOGLE_API_KEY"] = g_key

    p_key = os.getenv("PINECONE_API_KEY") or os.getenv("PINECONE_DB")
    if not p_key:
        p_key = getpass.getpass("Enter your Pinecone API Key (press Enter to skip and use local FAISS): ")
        if p_key:
            os.environ["PINECONE_API_KEY"] = p_key

    print("✅ API Keys configured! \n Please wait while loading vector store & LLM...\n")

    qa_chain = build_qa_chain()

    print("\n🤖 GitLab Chatbot (Terminal Mode with Pinecone DB). Type 'exit' to quit.\n")
    while True:
        question = input("\nYou: ")
        if question.lower() in ["exit", "quit"]:
            break
        try:
            result = qa_chain.invoke({"question": question})
            print("\nAssistant:", result["answer"], "\n")
        except Exception as e:
            print("⚠️ Error:", e)
