from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag import get_answer

app = FastAPI(title="GovGPT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "GovGPT Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = get_answer(request.question)
    print(answer)
    return {"answer": answer}