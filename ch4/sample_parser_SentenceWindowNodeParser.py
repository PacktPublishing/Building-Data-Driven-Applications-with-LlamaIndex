from llama_index.text_splitter import SentenceWindowNodeParser
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

parser = SentenceWindowNodeParser.from_defaults(
    window_size=2,  
    window_metadata_key="text_window",  
    original_text_metadata_key="original_sentence" 
)
nodes = parser.get_nodes_from_documents(document)

for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")