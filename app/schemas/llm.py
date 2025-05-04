from pydantic import BaseModel

class Question(BaseModel):
    prompt: str

class Answer(BaseModel):
    response: str

class StructuredResponse(BaseModel):
    response: str
