from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

title_extractor = TitleExtractor(summaries=["self"]) 
meta= title_extractor.extract(nodes)

print("\nFirst title: " +meta[0]['document_title'])
print("Second title: " +meta[1]['document_title'])

