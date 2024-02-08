from llama_index import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="index_cache")
index = load_index_from_storage(storage_context)
