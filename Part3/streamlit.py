import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Ensure parent path is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# Load .env file
root_env = BASE_DIR / ".env"
load_dotenv(dotenv_path=root_env)
load_dotenv()

from Part2.llm_integration import setup_api_key, build_qa_chain
import streamlit as st

# ✅ Streamlit Config
st.set_page_config("GitLab GenAI Chatbot", page_icon="🤖", layout="wide")

def safe_get_secret(key_name: str, default: str = None) -> str:
    """Safely fetch key from os.environ or st.secrets without throwing StreamlitSecretNotFoundError."""
    val = os.getenv(key_name)
    if val:
        return val
    try:
        if key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    return default

# ------------------------------
# 🔐 API Key Setup
# ------------------------------
google_api_key = safe_get_secret("GOOGLE_API_KEY")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key
else:
    st.error("⚠️ GOOGLE_API_KEY not found! Please set it in .env or Streamlit secrets.")
    st.stop()

pinecone_api_key = safe_get_secret("PINECONE_API_KEY") or safe_get_secret("PINECONE_DB")
if pinecone_api_key:
    os.environ["PINECONE_API_KEY"] = pinecone_api_key

pinecone_index = safe_get_secret("PINECONE_INDEX_NAME")
if pinecone_index:
    os.environ["PINECONE_INDEX_NAME"] = pinecone_index

# ------------------------------
# 🤖 Cached QA Chain Loader
# ------------------------------
@st.cache_resource(show_spinner="🌲 Connecting to Pinecone DB & loading AI Model...")
def get_qa_chain():
    return build_qa_chain()

qa_chain = get_qa_chain()

# ------------------------------
# 🖼️ Streamlit UI Setup
# ------------------------------
st.title("🤖 GitLab Handbook & Direction AI Chatbot")
st.markdown("""
Welcome! This GenAI assistant powered by **Pinecone DB** helps GitLab team members and future employees learn about:
- 📘 **GitLab's Handbook** (culture, engineering, async workflow, etc.)
- 🧭 **GitLab's Product Direction** (strategy, themes, FY25+)

Ask your question below and the chatbot will retrieve answers directly from official GitLab docs stored in Pinecone!
""")

# Chat session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.chat_input("Ask me anything about GitLab... ✨")

# Display past messages
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_msg)
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_msg)

# Handle new query
if user_query:
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_query)

    try:
        with st.spinner("🤖 Searching Pinecone DB & generating response..."):
            result = qa_chain.invoke({"question": user_query})
            response = result["answer"]

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)

        # Show sources
        with st.expander("📚 Sources & Retrieval Context", expanded=False):
            for doc in result.get("source_documents", []):
                meta = doc.metadata
                st.markdown(f"**{meta.get('source', 'Unknown')} →** `{meta.get('section', 'N/A')}`")
                st.code(doc.page_content.strip()[:700] + "...", language="markdown")

        st.session_state.chat_history.append((user_query, response))

    except Exception as e:
        st.error("⚠️ Something went wrong while generating the answer.")
        st.exception(e)
