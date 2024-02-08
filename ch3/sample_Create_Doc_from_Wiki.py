from llama_index import download_loader 

WikipediaReader = download_loader("WikipediaReader") 
loader = WikipediaReader() 
documents = loader.load_data(pages=['Pythagorean theorem','General relativity']) 