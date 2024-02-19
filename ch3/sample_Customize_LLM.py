from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
Settings.llm = OpenAI(temperature=0.8, model="gpt-4")

from llama_index.core.schema import TextNode
from llama_index.core import SummaryIndex

nodes = [
  TextNode(text="Lionel Messi's hometown is Rosario."),
  TextNode(text="He was born on June 24, 1987.")
]
index = SummaryIndex(nodes)
query_engine = index.as_query_engine()
response = query_engine.query(
    "What is Messi's hometown?"
)
print(response)