from llama_index.core.schema import TextNode
from llama_index.core.settings import Settings
from llama_index.core import SummaryIndex
from llama_index.llms.openai import OpenAI

Settings.llm = OpenAI(temperature=0.8, model="gpt-4")

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