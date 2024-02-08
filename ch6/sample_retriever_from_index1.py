from llama_index import SummaryIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
summary_index = SummaryIndex.from_documents(documents)
retriever = summary_index.as_retriever(
retriever_mode='embedding'
)
