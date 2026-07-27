import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

embedding = None
retriever = None


def get_retriever():
    global embedding, retriever

    if retriever is None:
        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        db = Chroma(
            persist_directory="chroma_db",
            embedding_function=embedding
        )

        retriever = db.as_retriever(search_kwargs={"k": 4})

    return retriever


def get_answer(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    prompt = f"""
You are GovGPT.

You are an AI assistant for Indian Government services.

Answer ONLY using the provided context.

If unavailable, reply:
"I couldn't find this information in the official documents."

Give the answer in stepwise bullet form.
Bold important keywords.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text