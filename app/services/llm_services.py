from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from app.schemas.llm import StructuredResponse

def messages(query: str):
    return [
        ChatMessage(role="system", content="You are a helpful assistant"),
        ChatMessage(role="user", content=query)
    ]

def chat(query: str):
    prompt = messages(query=query)
    llm = Ollama(model="deepseek-r1:1.5b", request_timeout=120.0)
    structured_llm = llm.as_structured_llm(StructuredResponse)
    response = structured_llm.chat(messages=prompt)
    return response.message.content
