from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader(
    input_dir="files",
    recursive=True
)
documents = reader.load_data()
for doc in documents:
    print(doc.metadata)

