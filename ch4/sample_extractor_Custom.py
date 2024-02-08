from llama_index.readers import SimpleDirectoryReader
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import BaseExtractor

class CustomExtractor(BaseExtractor):
    def extract(self, nodes):
        metadata_list = [
            {
                "node_length":  str(len(node.text))
            }
            for node in nodes
        ]
    return metadata_list

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

extractor = CustomExtractor()
metadata_list = extractor.extract(nodes)

print(metadata_list)

