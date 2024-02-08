from llama_index.text_splitter import TokenTextSplitter
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

splitter = TokenTextSplitter(
    chunk_size = 25
    chunk_overlap = 2,
    separator = " ",
    backup_separators = [".", "!", "?"]
)
nodes = splitter.get_nodes_from_documents(documents)

for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")