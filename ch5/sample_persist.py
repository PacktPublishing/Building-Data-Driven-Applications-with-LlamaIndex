from llama_index import VectorStoreIndex, SimpleDirectoryReader  
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist(persist_dir="index_cache")
