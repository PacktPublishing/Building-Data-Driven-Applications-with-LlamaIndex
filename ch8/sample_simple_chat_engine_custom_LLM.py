from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.llms.openai import OpenAI

llm = OpenAI(temperature=0.8, model="gpt-4")
chat_engine = SimpleChatEngine.from_defaults(llm=llm)   
chat_engine.chat_repl()
