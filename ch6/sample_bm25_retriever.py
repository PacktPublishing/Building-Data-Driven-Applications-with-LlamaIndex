from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
reader = SimpleDirectoryReader('files')
documents = reader.load_data()
splitter = SentenceSplitter.from_defaults(
    chunk_size=60, 
    chunk_overlap=0, 
    include_metadata=False
)
nodes = splitter.get_nodes_from_documents(
    documents
)

retriever = BM25Retriever.from_defaults(
    nodes=nodes, 
    similarity_top_k=2
)
response = retriever.retrieve("Who built the Colosseum?")
for node_with_score in response:
    print('Text:'+node_with_score.node.text)
    print('Score: '+str(node_with_score.score))

