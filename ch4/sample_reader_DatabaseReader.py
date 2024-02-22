from llama_index.readers.database import DatabaseReader
reader = DatabaseReader(
    uri="sqlite:///files/db/example.db"
)
query = "SELECT * FROM products"
documents = reader.load_data(query=query)
for doc in documents:
    print(doc.text)

