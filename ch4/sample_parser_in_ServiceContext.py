from llama_index import ServiceContext, Document, VectorStoreIndex
from llama_index.node_parser import SentenceWindowNodeParser

doc = Document(text="Sentence 1. Sentence 2. Sentence 3.")
text_splitter = SentenceWindowNodeParser.from_defaults(
    window_size=2  ,
    window_metadata_key="ContextWindow",
    original_text_metadata_key="node_text"
    )

service_context = ServiceContext.from_defaults(text_splitter=text_splitter)
index = VectorStoreIndex.from_documents([doc],service_context=service_context)
