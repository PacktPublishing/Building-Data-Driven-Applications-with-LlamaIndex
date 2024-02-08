from llama_index.text_splitter import CodeSplitter
from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("sample_GitHubRepositoryReader.py"))

code_splitter = CodeSplitter.from_defaults(
    language = 'python',  
    chunk_lines = 10, 
    chunk_lines_overlap = 5,   
    max_chars = 1000
)
nodes = code_splitter.get_nodes_from_documents(documents)

for node in nodes:
    print(f"Metadata {node.metadata} \nText {node.text}")