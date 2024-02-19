from llama_index.core import Document

text = "The quick brown fox jumps over the lazy dog."
doc = Document(
    text=text, 
    metadata={'author': 'John Doe','category': 'others'}, 
    id_='1'
)
print(doc)