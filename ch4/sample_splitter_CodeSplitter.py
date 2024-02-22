from llama_index.core.node_parser import CodeSplitter
from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("sample_reader_GitHubRepositoryReader.py"))

code_splitter = CodeSplitter.from_defaults(
    language = 'python',  
    chunk_lines = 5, 
    chunk_lines_overlap = 2,   
    max_chars = 150
)
nodes = code_splitter.get_nodes_from_documents(document)

for node in nodes:
    print(f"Metadata {node.metadata} \nText: {node.text}\n")
