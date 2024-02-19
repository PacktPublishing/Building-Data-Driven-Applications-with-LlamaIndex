from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import QuestionsAnsweredExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

qa_extractor = QuestionsAnsweredExtractor(questions=5)
metadata_list = qa_extractor.extract(nodes)

print(metadata_list)