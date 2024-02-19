from llama_index.core import KeywordTableIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
index = KeywordTableIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What famous buildings were in ancient Rome?")
print(response)
