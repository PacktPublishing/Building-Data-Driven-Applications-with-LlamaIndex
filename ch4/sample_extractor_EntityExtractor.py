from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.extractors.entity import EntityExtractor

reader = SimpleDirectoryReader('files')
documents = reader.load_data()
parser = SentenceSplitter(include_prev_next_rel=True)
nodes = parser.get_nodes_from_documents(documents)

entity_extractor = EntityExtractor(
    label_entities = True,
    device = "cpu"
)
metadata_list = entity_extractor.extract(nodes)

print(metadata_list)

# de mentionat ca necesita torch:
# - daca exista CUDA instalat, atunci torch se instaleaza cu: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# - daca nu exista CUDA, atunci torch se instaleaza cu: pip install torch torchvision torchaudio
# in functie de cuda sau , trebuie modificat parametrul device cuda/cpu
# de mentionat ca necesita span_marker: pip install span-marker