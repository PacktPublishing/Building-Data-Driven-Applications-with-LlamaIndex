from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist(persist_dir="index_cache")
print("Index persisted to disk.")