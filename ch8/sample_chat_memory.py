from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.memory import ChatMemoryBuffer

try:
    chat_store = SimpleChatStore.from_persist_path(
        persist_path="chat_memory.json"
    )
except FileNotFoundError:
    chat_store = SimpleChatStore()


memory = ChatMemoryBuffer.from_defaults(
    token_limit=2000,
    chat_store=chat_store,
    chat_store_key="user_X"
    )  

chat_engine = SimpleChatEngine.from_defaults(memory=memory)
while True:
    user_message = input("You: ")
    if user_message.lower() == 'exit':
        print("Exiting chat...")
        break
    response = chat_engine.chat(user_message)
    print(f"Chatbot: {response}")

chat_store.persist(persist_path="chat_memory.json")
