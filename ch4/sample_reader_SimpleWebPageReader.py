from llama_index.readers.web import SimpleWebPageReader

urls = ["https://docs.llamaindex.ai"]
documents = SimpleWebPageReader().load_data(urls)

for doc in documents:
    print(doc.text)
