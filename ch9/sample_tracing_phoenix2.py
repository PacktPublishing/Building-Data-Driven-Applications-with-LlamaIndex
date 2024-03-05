from llama_index.core import (
    SimpleDirectoryReader, 
    VectorStoreIndex, 
    set_global_handler
)
import phoenix as px

px.launch_app()
set_global_handler("arize_phoenix")

documents = SimpleDirectoryReader('files').load_data()
index = VectorStoreIndex.from_documents(documents)
qe = index.as_query_engine()
response = qe.query("Tell me about ancient Rome")
print(response)

input("Press <ENTER> to exit...")
