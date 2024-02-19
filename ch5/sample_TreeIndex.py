from llama_index.core import TreeIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
index = TreeIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Tell me about dogs")
print(response)
