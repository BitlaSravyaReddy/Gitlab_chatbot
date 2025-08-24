# Code Snippets and Line-by-Line Explanation

This document breaks down every important part of the code to help you understand exactly how this AI chatbot works. We'll go through both main files: the vector store builder and the chat application.

## File 1: build_vector_store.py - The Data Preparation Engine

This file takes raw text documents and transforms them into a searchable AI database.




### Import Section
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path
```
**What each line does:**
- **Line 1**: Imports a smart text splitter that breaks documents into chunks while keeping related sentences together
- **Line 2**: Imports the system that converts text into mathematical vectors (embeddings) using HuggingFace models
- **Line 3**: Imports FAISS, a high-performance database for storing and searching through vectors
- **Line 4**: Imports Path for easy file handling

**What would happen if we used something else:**
- Without RecursiveCharacterTextSplitter, we might break sentences in the middle, making the AI give incomplete answers
- Without HuggingFace embeddings, we'd need to train our own model (extremely expensive and time-consuming)
- Without FAISS, simple keyword search would miss the meaning and context of questions 





### Loading the Documents
```python
handbook_text = Path("Part1/data/handbook_cleaned_FULL.txt").read_text(encoding="utf-8")
direction_text = Path("Part2/data/direction_final.txt").read_text(encoding="utf-8")
```

**What each line does:**
- **Line 1**: Reads the entire GitLab handbook (500,000+ words) into memory as a string
- **Line 2**: Reads GitLab's strategic direction document into memory

**What would happen if we used something else:**
- If we didn't specify `encoding="utf-8"`, special characters might display incorrectly
- If we tried to process the files line by line instead of loading completely, we'd lose the ability to understand context across paragraphs.






### Setting Up the Text Splitter
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=150,
    length_function=len,
)
```

**What each line does:**
- **Line 1**: Creates an intelligent text splitter object
- **Line 2**: Sets each chunk to about 750 characters (roughly 150 words)
- **Line 3**: Makes chunks overlap by 150 characters to preserve context between chunks
- **Line 4**: Uses simple character counting to measure length

**What would happen if we used different numbers:**
- **Smaller chunk_size (300)**: More precise retrieval but might lose broader context
- **Larger chunk_size (1500)**: Better context but might include irrelevant information
- **No overlap (0)**: Risk of splitting important information across chunks
- **Too much overlap (400)**: Redundant information, slower search, higher costs

### The Chunking Function with Metadata
```python
def chunk_with_metadata(text, source_label):
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
```

**Breaking this down line by line:**

**Line 1**: Defines a function that takes text and a label for where it came from
**Line 2**: Splits the text at "## SECTION:" markers (this is how the documents are organized)
**Line 3**: Creates an empty list to store the processed document chunks

**Line 5**: Starts a loop through each section
**Line 6-7**: Skips empty sections to avoid processing nothing
**Line 8**: Separates the section header from the content using Python's unpacking
**Line 9**: Gets the body text, or empty string if there's no content
**Line 10**: Uses the text splitter to break the section into appropriately-sized chunks
**Line 11-15**: Adds metadata to each chunk so we know where it came from
**Line 16**: Adds all chunks from this section to our master list
**Line 17**: Returns all the processed documents

**What would happen with different approaches:**
- **Without metadata**: The AI couldn't tell users where information came from
- **Without section splitting**: Related information might be scattered across random chunks
- **Different splitting markers**: Would need to match how the source documents are actually formatted




### Creating the Documents
```python
handbook_docs = chunk_with_metadata(handbook_text, "handbook")
direction_docs = chunk_with_metadata(direction_text, "direction")
all_docs = handbook_docs + direction_docs
print(f"✅ Total chunks: {len(all_docs)}")
```
**What each line does:**
- **Line 1**: Processes the handbook text into searchable chunks tagged as "handbook"
- **Line 2**: Processes the direction text into searchable chunks tagged as "direction"
- **Line 3**: Combines both sets of documents into one master collection
- **Line 4**: Prints how many chunks were created (helps verify the process worked)




### Creating the Embeddings Model
```python
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

**What this line does:**
- Creates an embedding model that converts text into 384-dimensional vectors
- Uses a pre-trained model that's good at understanding sentence meaning
- This specific model is fast, lightweight, and works well for question-answering

**What would happen with different models:**
- **Larger models (all-mpnet-base-v2)**: Better accuracy but slower and more memory-intensive
- **Smaller models**: Faster but might miss subtle meaning differences
- **OpenAI embeddings**: More expensive, requires API calls, but might be more accurate  



### Creating and Saving the Vector Database
```python
vectordb = FAISS.from_documents(all_docs, embedding_model)
vectordb.save_local("data/faiss_index")
print("✅ FAISS index saved to: data/faiss_index/")
```
**What each line does:**
- **Line 1**: Creates a FAISS vector database from all documents using the embedding model
- **Line 2**: Saves the database to disk so we don't have to rebuild it every time
- **Line 3**: Confirms the save was successful

**What's happening behind the scenes:**
1. Each text chunk gets converted to a 384-dimensional vector
2. FAISS builds an index that allows fast similarity search
3. The index and metadata get saved as files on disk

---