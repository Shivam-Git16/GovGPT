import os

from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = db.as_retriever(
    search_kwargs={"k": 4}
)


def get_answer(question):

    docs = retriever.invoke(question)

    context = ""

    for doc in docs:
        context += doc.page_content
        context += "\n\n"

    prompt = f"""
You are GovGPT.

You are an AI assistant for Indian Government services.

Answer ONLY using the provided context.

If the answer is unavailable say
Give answer in stepwise in bullet form, Bold the important keyword

"I couldn't find this information in the official documents."

Return answer in markdown.
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