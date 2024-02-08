from llama_index.readers import SimpleDirectoryReader
from llama_index.extractors import SummaryExtractor,QuestionsAnsweredExtractor
from llama_index.text_splitter import TokenTextSplitter
from llama_index.ingestion import IngestionPipeline, IngestionCache
from llama_index.schema import TransformComponent

class CustomTransformation(TransformComponent):
  def __call__(self, nodes, **kwargs):
    # run any node transformation logic here
    return nodes
    
reader = SimpleDirectoryReader('files')
documents = reader.load_data()
try: 
    cached_hashes = IngestionCache.from_persist_path(
"./ingestion_cache.json"
)
    print("Cache file found. Running using cache...")
except:
    cached_hashes = ""
    print("No cache file found. Running without cache...")

pipeline = IngestionPipeline(
    transformations = [
        CustomTransformation(),
        TokenTextSplitter(
            separator=" ", 
            chunk_size=512, 
            chunk_overlap=128), 
        SummaryExtractor(), 
        QuestionsAnsweredExtractor(
            questions=3
        )
    ],
    cache=cached_hashes
)

nodes = pipeline.run(documents=documents, show_progress=True)
pipeline.cache.persist("./ingestion_cache.json")


