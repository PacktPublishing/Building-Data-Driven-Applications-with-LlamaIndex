from llama_index.core import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="index_cache")
index = load_index_from_storage(storage_context)

print("Index loaded successfully!")
