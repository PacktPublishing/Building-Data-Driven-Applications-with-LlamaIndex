from llama_index.core.node_parser import HTMLNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/others/sample.html"))

my_tags = ["p", "span"]  
html_parser = HTMLNodeParser(tags=my_tags)
nodes = html_parser.get_nodes_from_documents(document)

print('<span> elements:')
for node in nodes:
    if node.metadata['tag']=='span':
        print(node.text)
 
print('<p> elements:') 
for node in nodes:
    if node.metadata['tag']=='p':
        print(node.text)