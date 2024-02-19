from llama_index.core.chat_engine import SimpleChatEngine
chat_engine = SimpleChatEngine.from_defaults()
chat_engine.chat_repl()
