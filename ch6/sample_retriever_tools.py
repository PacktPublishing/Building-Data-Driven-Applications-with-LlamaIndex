from llama_index.core.selectors import PydanticMultiSelector
from llama_index.core.retrievers import RouterRetriever
from llama_index.core.tools import RetrieverTool
from llama_index.core import VectorStoreIndex, SummaryIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("files").load_data()

vector_index = VectorStoreIndex.from_documents([documents[0]])
summary_index = SummaryIndex.from_documents([documents[1]])

vector_retriever = vector_index.as_retriever()
summary_retriever = summary_index.as_retriever()

vector_tool = RetrieverTool.from_defaults(
    retriever=vector_retriever,
    description="Use this for answering questions about Ancient Rome"
)
summary_tool = RetrieverTool.from_defaults(
    retriever=summary_retriever,
    description="Use this for answering questions about dogs"
)

retriever = RouterRetriever(
    selector=PydanticMultiSelector.from_defaults(),
    retriever_tools=[
        vector_tool,
        summary_tool
    ]
)
response = retriever.retrieve(
    "What can you tell me about the Ancient Rome?"
)
for r in response:
    print(r.text)

'''
#other possible queries
retriever.retrieve("What can you tell me about the Ancient Rome?") 
retriever.retrieve("Tell me all you know about dogs") 
retriever.retrieve("Tell me abous dogs in Ancient Rome")
'''