from llama_index import download_loader

MapReader = download_loader("OpenMap")
loader = MapReader()
documents = loader.load_data(
    localarea='Paris', 
    search_tag='tourism', 
    tag_only=True, 
    local_area_buffer=2000, 
    tag_values=['museum']
)
