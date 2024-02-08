from llama_index.readers import SimpleDirectoryReader
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import EntityExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

entity_extractor = EntityExtractor(
    label_entities = True,
    device = "cuda"
)
metadata_list = entity_extractor.extract(nodes)

print(metadata_list)