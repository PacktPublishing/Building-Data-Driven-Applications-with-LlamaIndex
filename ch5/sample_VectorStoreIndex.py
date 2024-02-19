from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
index = VectorStoreIndex.from_documents(documents)
print("Index created successfully!")
