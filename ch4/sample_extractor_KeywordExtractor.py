from llama_index.readers import SimpleDirectoryReader
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import KeywordExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

key_extractor = KeywordExtractor(keywords=3)
metadata_list = key_extractor.extract(nodes)

print(metadata_list)
