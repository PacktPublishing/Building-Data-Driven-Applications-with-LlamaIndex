from llama_index.core.vector_stores import MetadataFilter, MetadataFilters
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import TextNode
user_departments = {"Alice": "Security", "Bob": "IT"}

nodes = [
    TextNode(
        text=(
            "An incident is an accidental or malicious event that has the potential to cause unwanted effects on the security of our IT assets."),
        metadata={"department": "Security"},
    ),
    TextNode(
        text=("An incident is an unexpected interruption or degradation of an IT service."),
        metadata={"department": "IT"},
    )
]

def show_report(index, user, query):
    user_department = user_departments[user]
    filters = MetadataFilters(
        filters=[
            MetadataFilter(key="department", value=user_department)
        ]
    )
    retriever = index.as_retriever(filters=filters)
    response = retriever.retrieve(query)
    print(f"Response for {user}: {response[0].node.text}")


index = VectorStoreIndex(nodes)
query = "What is an incident?"
show_report(index, "Alice", query)
show_report(index, "Bob", query)
