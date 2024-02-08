from llama_index import download_loader

DatabaseReader = download_loader('DatabaseReader')
reader = DatabaseReader(
    uri="sqlite:///example.db"
)
query = "SELECT * FROM products"
documents = reader.load_data(query=query)
