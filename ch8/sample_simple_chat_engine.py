from llama_index.chat_engine import SimpleChatEngine
chat_engine = SimpleChatEngine.from_defaults()
chat_engine.chat_repl()
