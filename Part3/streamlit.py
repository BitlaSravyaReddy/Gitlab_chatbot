import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Part2.llm_integration import setup_api_key, build_qa_chain

import streamlit as st
# ✅ Streamlit Config
st.set_page_config("GitLab GenAI Chatbot", page_icon="🤖", layout="wide")

# ------------------------------
# 🔐 API Key Setup
# ------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    setup_api_key(st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Google API Key not found. Please add it to Streamlit secrets.")
    st.stop()

# ------------------------------
# 🤖 Load QA Chain
# ------------------------------
qa_chain = build_qa_chain()

# ------------------------------
# 🖼️ Streamlit UI Setup
# ------------------------------
st.title("🤖 GitLab Handbook & Direction AI Chatbot")
st.markdown("""
Welcome! This GenAI assistant helps GitLab team members and future employees learn about:
- 📘 GitLab's Handbook (culture, engineering, async, etc.)
- 🧭 GitLab's Product Direction (strategy, themes, FY25+)

Just ask your question below and the chatbot will find answers from official GitLab docs.
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
        with st.spinner("🤖 Thinking... generating response..."):
            result = qa_chain({"question": user_query})
            response = result["answer"]

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)

        # Show sources
        with st.expander("📚 Sources & Reasoning", expanded=False):
            for doc in result.get("source_documents", []):
                meta = doc.metadata
                st.markdown(f"**{meta.get('source', 'Unknown')} →** `{meta.get('section', 'N/A')}`")
                st.code(doc.page_content.strip()[:700] + "...", language="markdown")

        st.session_state.chat_history.append((user_query, response))

    except Exception as e:
        st.error("⚠️ Something went wrong while generating the answer.")
        st.exception(e)
