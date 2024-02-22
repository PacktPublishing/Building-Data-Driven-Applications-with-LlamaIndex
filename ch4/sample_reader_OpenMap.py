from llama_index.readers.maps import OpenMap

loader = OpenMap()
documents = loader.load_data(
    localarea='Paris', 
    search_tag='tourism', 
    tag_only=True, 
    local_area_buffer=2000, 
    tag_values=['museum']
)
print(documents)