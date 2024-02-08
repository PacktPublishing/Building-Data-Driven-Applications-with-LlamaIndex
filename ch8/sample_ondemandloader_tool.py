from llama_index import download_loader
from llama_index.agent import OpenAIAgent
from llama_index.tools.ondemand_loader_tool import OnDemandLoaderTool

WikipediaReader = download_loader("WikipediaReader")

tool = OnDemandLoaderTool.from_defaults(
 WikipediaReader(),
 name="WikipediaReader",
 description="args: {'pages': [<list of pages>],'query_str': <query>}"           
)

agent = OpenAIAgent.from_tools(
    tools=[tool], 
    verbose=True
)
response = agent.chat(
    "What were some famous buildings in ancient Rome?")
print(response)
