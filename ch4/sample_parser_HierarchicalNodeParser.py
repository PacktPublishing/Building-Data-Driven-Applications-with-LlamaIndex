from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

hierarchical_parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[128, 64, 32],  
    chunk_overlap=0,              
)
nodes = hierarchical_parser.get_nodes_from_documents(document)


for node in nodes:
    print(f"Metadata: {node.metadata} \nText: {node.text}")
    