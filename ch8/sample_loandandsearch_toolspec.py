from llama_index.core.tools.tool_spec.load_and_search.base import LoadAndSearchToolSpec
from llama_index.tools.database import DatabaseToolSpec
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI

db_tools = DatabaseToolSpec(uri="sqlite:///files//database//employees.db")
tool_list = db_tools.to_tool_list()
tools=LoadAndSearchToolSpec.from_defaults(tool_list[0]).to_tool_list()

llm = OpenAI(model="gpt-4")
agent = OpenAIAgent.from_tools(
    tools=tools, 
    llm=llm, 
    verbose=True
)
response = agent.chat(
    "Who has the highest salary in the Employees table?'")
print(response)
