from llama_index.llms import OpenAI
from llama_index import ServiceContext 

llm = OpenAI(temperature=0.8, model="gpt-4")
service_context = ServiceContext.from_defaults(llm=llm)
