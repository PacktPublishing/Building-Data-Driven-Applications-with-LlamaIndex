from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

title_extractor = TitleExtractor()
metadata_list = title_extractor.extract(nodes) 

print(metadata_list)
