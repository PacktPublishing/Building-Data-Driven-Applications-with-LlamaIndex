from llama_index.core import KnowledgeGraphIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
index = KnowledgeGraphIndex.from_documents(documents, max_triplets_per_chunk=2, use_async=True)
query_engine = index.as_query_engine()
response = query_engine.query("Tell me about dogs.")
print(response)
