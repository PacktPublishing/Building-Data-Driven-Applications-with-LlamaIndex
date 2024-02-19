from llama_index.core.retrievers import SummaryIndexEmbeddingRetriever
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import SummaryIndex, SimpleDirectoryReader, get_response_synthesizer

documents = SimpleDirectoryReader("files").load_data()
index = SummaryIndex.from_documents(documents)

retriever = SummaryIndexEmbeddingRetriever(
    index=index,
    similarity_top_k=3,
)
response_synthesizer = get_response_synthesizer(
    response_mode="tree_summarize",
    verbose=True
)
pp = SimilarityPostprocessor(similarity_cutoff=0.7)

query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[pp]
)
response = query_engine.query(
    "Enumerate iconic buildings in ancient Rome"
)
print(response)
