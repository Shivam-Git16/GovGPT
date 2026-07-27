import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Loading PDFs...")

loader = PyPDFDirectoryLoader("data")

documents = loader.load()

print("Documents Loaded:", len(documents))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print("Chunks Created:", len(chunks))

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating Vector Database...")

db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("Done!")
print("Vector Database Saved Successfully.")