from llama_index.core import Document, SummaryIndex
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.readers.wikipedia import WikipediaReader

loader = WikipediaReader()
documents = loader.load_data(
    pages=['Messi Lionel']
)
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)
index = SummaryIndex(nodes)
query_engine = index.as_query_engine()
print("Ask me anything about Lionel Messi!")

while True:
	question = input(
        "What would you like to know about Lionel Messi? "
    )
	response = query_engine.query(question)
	print(response)

#this is not a true Chat as it doesn't retain conversation history
#should be replaced with something simpler