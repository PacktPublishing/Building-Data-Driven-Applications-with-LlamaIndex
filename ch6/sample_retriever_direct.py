from llama_index.core import SummaryIndex, SimpleDirectoryReader
from llama_index.core.retrievers import SummaryIndexEmbeddingRetriever

documents = SimpleDirectoryReader("files").load_data()
summary_index = SummaryIndex.from_documents(documents)
retriever = SummaryIndexEmbeddingRetriever(
    index=summary_index
)
result = retriever.retrieve("Tell me about ancient Rome")
print(result[0].text)
