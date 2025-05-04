from fastapi import APIRouter
from app.schemas.llm import Question, Answer
from app.services.llm_services import chat

router = APIRouter()

@router.post("/chat", response_model=Answer)
def ask_question(query: Question):
    answer_text = chat(query=query.question)
    return {"answer": answer_text}
