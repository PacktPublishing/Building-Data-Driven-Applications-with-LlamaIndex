from llama_index.readers import SimpleDirectoryReader
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import SummaryExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

summary_extractor = SummaryExtractor(summaries=["prev", "self", "next"]) 
metadata_list = summary_extractor.extract(nodes)

print(metadata_list)