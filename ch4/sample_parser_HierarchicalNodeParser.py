from llama_index.text_splitter import HierarchicalNodeParser
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

hierarchical_parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[512, 256, 128],  
    chunk_overlap=100,              
)
nodes = hierarchical_parser.get_nodes_from_documents(document)


for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")