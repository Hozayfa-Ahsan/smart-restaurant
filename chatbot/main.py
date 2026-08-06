from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from chatbot.rag_pipeline import RAGPipeline

app = FastAPI(
    title="Foodie Restaurant AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = RAGPipeline()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "status": "running",
        "service": "Restaurant AI Chatbot"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = rag.ask(request.message)

    return {
        "answer": result["answer"]
    }