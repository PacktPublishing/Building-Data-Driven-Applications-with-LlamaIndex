from llama_index.core import Document
from llama_index.core.node_parser import SentenceWindowNodeParser
doc = Document(
    text="Sentence 1. Sentence 2. Sentence 3."
)
parser = SentenceWindowNodeParser.from_defaults(
    window_size=2  ,
    window_metadata_key="ContextWindow",
    original_text_metadata_key="node_text"
)
nodes = parser.get_nodes_from_documents([doc])
print(nodes[1]) 
print(nodes[1].metadata) 