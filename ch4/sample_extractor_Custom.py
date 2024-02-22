from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import BaseExtractor
from typing import List, Dict

class CustomExtractor(BaseExtractor):
    async def aextract(self, nodes) -> List[Dict]:
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
print(extractor.extract(nodes))
