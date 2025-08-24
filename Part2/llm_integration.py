# llm_integration.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
import getpass
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_google_genai")


# 🔐 API Key Setup
def setup_api_key(google_api_key: str):
    os.environ["GOOGLE_API_KEY"] = google_api_key


# 🧠 Load FAISS Vector DB & Retriever
def load_vector_store():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.load_local(
        "Part1/data/faiss_index",
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
        model="gemini-1.5-flash",
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
    secret = getpass.getpass("Enter your Google API Key: ")
    api_key = os.getenv("GOOGLE_API_KEY") or secret
    setup_api_key(api_key)

    print("✅ API key accepted! \n Please wait while loading...\n")

    qa_chain = build_qa_chain()

    print("\n🤖 GitLab Chatbot (Terminal Mode). Type 'exit' to quit.\n")
    while True:
        question = input("\nYou: ")
        if question.lower() in ["exit", "quit"]:
            break
        try:
            result = qa_chain.invoke({"question": question})
            print("\nAssistant:", result["answer"], "\n")
        except Exception as e:
            print("⚠️ Error:", e)
