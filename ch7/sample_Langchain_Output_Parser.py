from pydantic import BaseModel
from typing import List
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from llama_index.output_parsers import LangchainOutputParser
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from llama_index.schema import Node

nodes = [
    Node(
        text="Roses have vibrant colors and smell nice."),
    Node(
        text="Oak trees are tall and have green leaves."),
]

schemas = [
    ResponseSchema(
        name="answer", 
        description=(
            "answer to the user's question"
        )
    ),
    ResponseSchema(
        name="source",
        description=(
            "the source text used to answer the user's question, "
            "should be a quote from the original prompt."
        )
    )
]

lc_parser = StructuredOutputParser.from_response_schemas(schemas)
output_parser = LangchainOutputParser(lc_parser)

llm = OpenAI(output_parser=output_parser)
sc = ServiceContext.from_defaults(llm=llm)

index = VectorStoreIndex(nodes=nodes)
query_engine = index.as_query_engine(service_context=sc)
response = query_engine.query(
    "Are oak trees small? yes or no",
)
print(response)
