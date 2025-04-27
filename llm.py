
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(
        role="user", content="do you know alharet?"
    )
]

llm = Ollama(model="deepseek-r1:1.5b", request_timeout=120.0)

resp = llm.stream_chat(messages=messages)

for r in resp:
    print(r.delta, end="")


