import chromadb
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader


db = chromadb.PersistentClient(path="chroma_database")
chroma_collection = db.get_or_create_collection(
    "my_chroma_store"
)

vector_store = ChromaVectorStore(
    chroma_collection=chroma_collection
)
storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

documents = SimpleDirectoryReader("files").load_data()
index = VectorStoreIndex.from_documents(
    documents=documents, 
    storage_context=storage_context
)

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, 
    storage_context=storage_context
)
