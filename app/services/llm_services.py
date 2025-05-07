from llama_index.llms.ollama import Ollama
from app.schemas.llm import StructuredResponse

def chat(query: str):
    prompt = (
        "You are an expert programming tutor. When given a question, explain the answer in clear and detailed steps, and **always** finish with a summary containing only the final code inside a code block.\n"
        "Do not use phrases like 'Sure', 'Here is', or 'Note'. Be straight to the point.\n"
        "Format:\n"
        "- Explanation first.\n"
        "- Then: 'Summary code:' followed by only the final clean code in a code block.\n"
        "User question:\n"
        f"{query}"
    )

    llm = Ollama(model="deepseek-coder:6.7b", request_timeout=120.0)
    structured_llm = llm.as_structured_llm(StructuredResponse)

    response = structured_llm.complete(prompt)
    return response.text
