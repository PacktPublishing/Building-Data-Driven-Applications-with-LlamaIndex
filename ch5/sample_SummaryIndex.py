from llama_index.core import SummaryIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
index = SummaryIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("How many documents have you loaded?")
print(response)
