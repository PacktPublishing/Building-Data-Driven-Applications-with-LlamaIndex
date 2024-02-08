from llama_index import SimpleWebPageReader

urls = ["https://docs.llamaindex.ai/en/stable/getting_started/installation.html"]
documents = SimpleWebPageReader().load_data(urls)
