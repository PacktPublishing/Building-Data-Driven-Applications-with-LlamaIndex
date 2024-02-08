from llama_index.schema import Document

text = "The quick brown fox jumps over the lazy dog."
doc = Document(text=text, metadata={'author': 'John Doe','category': 'Sample Category'}, id_='1')
