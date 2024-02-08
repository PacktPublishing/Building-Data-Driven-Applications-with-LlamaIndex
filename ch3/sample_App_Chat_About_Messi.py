from llama_index import Document, SummaryIndex, download_loader  
from llama_index.node_parser import SimpleNodeParser

WikipediaReader = download_loader("WikipediaReader")
loader = WikipediaReader()
documents = loader.load_data(pages=['Messi Lionel'])
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)
index = SummaryIndex(nodes)
query_engine = index.as_query_engine()
print("Ask me anything about Lionel Messi!")

while True:
	question = input("What would you like to know about Lionel Messi? ")
	response = query_engine.query(question)
	print(response)
