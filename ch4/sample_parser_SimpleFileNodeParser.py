from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("files/sample_document1.txt"))

print(f"Metadata: {document[0].metadata}")
print(f"Text: {document[0].text}")

