from llama_index.core.node_parser import JSONNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/others/sample.json"))

json_parser = JSONNodeParser.from_defaults()
nodes = json_parser.get_nodes_from_documents(document)

for node in nodes:
    print(f"Metadata {node.metadata} \nText: {node.text}")