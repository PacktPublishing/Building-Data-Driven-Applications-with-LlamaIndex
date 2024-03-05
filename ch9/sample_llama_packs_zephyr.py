from llama_index.packs.zephyr_query_engine import ZephyrQueryEnginePack
from llama_index.core import SimpleDirectoryReader
reader = SimpleDirectoryReader('files')
documents = reader.load_data()
zephyr_qe = ZephyrQueryEnginePack(documents)
response=zephyr_qe.run(
    "Enumerate famous buildings in ancient Rome"
    )
print(response)