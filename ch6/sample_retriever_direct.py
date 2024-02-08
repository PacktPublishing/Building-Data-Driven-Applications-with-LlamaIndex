from llama_index import SummaryIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()
from llama_index.retrievers import SummaryIndexEmbeddingRetriever   
summary_index = SummaryIndex.from_documents(documents)
retriever = SummaryIndexEmbeddingRetriever(
    index=summary_index
)
