from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Document Q&A API is running"}

@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {"answer": answer}