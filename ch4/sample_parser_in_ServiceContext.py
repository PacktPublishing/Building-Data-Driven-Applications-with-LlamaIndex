from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceWindowNodeParser

doc = Document(text="Sentence 1. Sentence 2. Sentence 3.")
text_splitter = SentenceWindowNodeParser.from_defaults(
    window_size=2  ,
    window_metadata_key="ContextWindow",
    original_text_metadata_key="node_text"
    )

Settings.text_splitter=text_splitter
index = VectorStoreIndex.from_documents([doc])
print("Successfully created the Index!")
