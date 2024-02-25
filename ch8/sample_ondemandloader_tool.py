from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool
from llama_index.readers.wikipedia import WikipediaReader

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
