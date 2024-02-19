from llama_index.core import SummaryIndex, Document
from llama_index.core.schema import TextNode

nodes = [
  TextNode(
    text="Lionel Messi is a football player from Argentina."
    ),
  TextNode(
    text="He has won the Ballon d'Or trophy 7 times."
    ),
  TextNode(text="Lionel Messi's hometown is Rosario."),
  TextNode(text="He was born on June 24, 1987.")
]
index = SummaryIndex(nodes)

query_engine = index.as_query_engine()
response = query_engine.query(
    "What is Messi's hometown?"
)
print(response)