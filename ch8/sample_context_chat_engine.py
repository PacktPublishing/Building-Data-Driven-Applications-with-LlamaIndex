from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
docs = SimpleDirectoryReader(input_dir="files").load_data()
index = VectorStoreIndex.from_documents(docs)
chat_engine = index.as_chat_engine(
    chat_mode="context",
    system_prompt=(
        "You’re a chatbot, able to talk about "
        "general topics, as well as answering specific "
        "questions about ancient Rome."
    ),
)
chat_engine.chat_repl()
