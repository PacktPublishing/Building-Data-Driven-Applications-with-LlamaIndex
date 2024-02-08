from llama_index.text_splitter import MarkdownNodeParser
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/others/sample.md"))

parser = MarkdownNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)

for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")

