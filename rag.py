from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# STEP 1: Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# STEP 2: Split text
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# STEP 3: Convert to embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# STEP 4: Store in FAISS
db = FAISS.from_documents(docs, embeddings)

# STEP 5: Create QA system
def ask_question(query):
    docs = db.similarity_search(query)
    context = " ".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="tinyllama")

    
    prompt = f"""
    Answer the question briefly and clearly using only the context below.

    Context:
    {context}

    Question:
    {query}

    Answer in 1-2 sentences:
    """

    return llm.invoke(prompt)