from llama_index.text_splitter import SimpleFileNodeParser
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

parser = SimpleFileNodeParser()
nodes = parser.get_nodes_from_documents(documents)

for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")
