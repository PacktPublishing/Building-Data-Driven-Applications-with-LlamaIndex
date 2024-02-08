from llama_index import SimpleDirectoryReader

reader = SimpleDirectoryReader(
    input_dir="files",
    recursive=True
)
documents = reader.load_data()
