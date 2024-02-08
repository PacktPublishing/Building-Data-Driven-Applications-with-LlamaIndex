from llama_index.chat_engine import SimpleChatEngine
from llama_index.llms import OpenAI

llm = OpenAI(temperature=0.8, model="gpt-4")
chat_engine = SimpleChatEngine.from_defaults(llm=llm)   
chat_engine.chat_repl()
