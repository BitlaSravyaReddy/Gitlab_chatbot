## File 2: llm_integration.py - The backend for Chatbot

This file creates the RAG Bot that users interact with.

### Import All Required Libraries
```python
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

```

**What each import provides:**
- **Line 1**: Loads and queries the vector database we created for storing document embeddings.
- **Line 2**: Provides the same embedding model we used when building the FAISS database.
- **Line 3**: Smart memory that summarizes older conversations to preserve context. 
- **Line 4**: Pre-built chain that combines retrieval(from FAISS)with conversation(LLM responses)
- **Line 5**: Interface to Google's Gemini AI model
- **Line 6**: System for creating custom prompts
- **Line 7**: Operating system interface
- **Line 8**: Safely handles hidden password/API key input (e.g., entering API keys without displaying them).
- **Line 9-10**: Suppresses unnecessary warning messages from langchain_google_genai for cleaner output.


### Setting up API KEY for RAG Model
```
def setup_api_key(google_api_key: str):
    os.environ["GOOGLE_API_KEY"] = google_api_key

```
**Breaking this down:**
**Line 1**: Defines a function named setup_api_key that accepts one parameter google_api_key
**Line 2**: Stores the provided API key into the environment variable GOOGLE_API_KEY, so that other parts of the program (like the Gemini client) can automatically read and use i



### Loading the Vector Database with Caching
```python
def load_vector_store():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.load_local(
        "data/faiss_index",
        embedding,
        allow_dangerous_deserialization=True
    )

    retriever = vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 8, "fetch_k": 18}
    )
    return retriever

retriever = load_vector_store()
```

**Breaking this down:**

**Line 1**: Function definition with descriptive name
**Line 2**: Creates the same embedding model used when building the database
**Line 3-6**: Loads the saved FAISS database from disk
- `allow_dangerous_deserialization=True` is needed because FAISS files contain pickled data

**Line 8-11**: Configures how the database searches for relevant information
- `search_type="mmr"` uses Maximum Marginal Relevance (finds diverse, non-redundant results)
- `k=8` returns 8 most relevant chunks
- `fetch_k=18` initially finds 18 candidates, then picks the 8 most diverse

**Line 13**: Actually calls the function and stores the retriever

**What would happen with different settings:**
- **Without caching**: Database would reload every time someone refreshes, making the app very slow
- **search_type="similarity"**: Might return very similar chunks, giving repetitive answers
- **Lower k (3)**: Faster but might miss important context
- **Higher k (15)**: More context but slower responses and higher AI costs


### Setting Up the AI Model
```python
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    convert_system_message_to_human=True,
)
```

**What each line does:**
- **Line 1**: Creates a connection to Google's Gemini AI model
- **Line 2**: Specifies the "flash" version (faster, cheaper than pro version)
- **Line 3**: Sets temperature to 0.3 (creative enough for natural responses, controlled enough for accuracy)
- **Line 4**: Technical setting needed for compatibility with this version of LangChain

**Why these settings:**
- **gemini-1.5-flash**: Good balance of speed, cost, and quality
- **temperature=0.3**: Low enough for factual accuracy, high enough to avoid robotic responses
- **convert_system_message_to_human=True**: Ensures prompt compatibility

### Conversation Memory Setup
```python
memory = ConversationSummaryBufferMemory(
    llm=gemini_llm,
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"
)
```

**What each line does:**
- **Line 1**: Creates intelligent memory that summarizes old conversations
- **Line 2**: Uses the same AI model for summarization
- **Line 3**: Names the memory storage "chat_history"
- **Line 4**: Returns messages in a format the conversation chain expects
- **Line 5**: Specifies which part of AI responses to remember (prevents confusion with multiple outputs)

**How this memory works:**
1. Keeps recent conversation turns in full detail
2. Summarizes older conversations to save space
3. Provides relevant context without hitting token limits

### Custom Prompt Template
```python
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an expert assistant trained on GitLab's official Handbook and Direction documents.

Please:
- Answer with as much useful detail as possible.
- Use bullet points or formatting if appropriate.
- Cite the source section when available.
- Only answer from GitLab materials. Politely decline anything off-topic.

Context:
{context}

Question:
{question}
"""
)
```

**What each part does:**
- **Line 1-2**: Defines a template that takes "context" and "question" as inputs
- **Lines 4-11**: Instructions that guide the AI's behavior
- **Lines 13-16**: Shows where the retrieved context and user question get inserted

**Why this specific prompt:**
- **Clear role definition**: AI knows it's a GitLab expert
- **Specific instructions**: Tells AI how to format responses
- **Safety guardrails**: Prevents off-topic or harmful responses
- **Context integration**: Shows how to use retrieved information

### Creating the Conversation Chain
```python
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=gemini_llm,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": prompt},
    output_key="answer",
    verbose=False
)
```

**What each parameter does:**
- **llm**: The AI model that generates responses
- **retriever**: The system that finds relevant document chunks
- **memory**: Remembers conversation history
- **return_source_documents=True**: Includes source citations
- **combine_docs_chain_kwargs**: Uses our custom prompt
- **output_key="answer"**: Prevents confusion when chain returns multiple outputs
- **verbose=False**: Keeps logs clean for production

**What this chain does automatically:**
1. Takes user question
2. Searches vector database for relevant context
3. Combines context with conversation history
4. Generates response using AI model
5. Updates conversation memory
6. Returns answer with sources


```
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

```


**What each part does:**
- **Line 1**: Ensures this block only runs when the script is executed directly (not when imported in Streamlit).
- **Lines 2**: Prompts the user securely for their Google API key (getpass.getpass) without showing it on the screen.
- **Lines 3**: Checks if GOOGLE_API_KEY is already in environment variables; if not, uses the user input.
- **Line  4**: Calls setup_api_key() to set the API key inside os.environ so Gemini can access it.
- **Lines 5**: Prints a confirmation message that the API key is accepted and that loading will start.
- **Line  6**: Calls build_qa_chain() to initialize the retriever, Gemini model, memory, and prompt for the chatbot.
- **Lines 7**: Prints chatbot startup instructions for terminal use.
- **Line 8-11**: Starts a loop to keep asking the user for input until they type exit or quit.
- **Lines 12**: Begins error handling (try block).
- **Line  13**: Sends the user’s question into the chain using .invoke() and stores the result.
- **Lines 14**: Prints the assistant’s answer back to the terminal.
- **Line 15-16**: Handles errors gracefully if something goes wrong (e.g., missing API key, retriever issue).

**Why this specific prompt:**
- **Clear role definition**: AI knows it's a GitLab expert
- **Specific instructions**: Tells AI how to format responses
- **Safety guardrails**: Prevents off-topic or harmful responses
- **Context integration**: Shows how to use retrieved information
- **Direct execution check**: Keeps this logic separate so the same file can be imported in Streamlit without running terminal mode.
- **Secure API key handling**: Uses getpass and environment variables for safety.
- **User-friendly feedback**: Prints clear status and instructions for the user.
- **Reusability**: Same chatbot pipeline works in both terminal and Streamlit with no code duplication.
- **Robustness**: Error handling prevents program crashes during runtime.