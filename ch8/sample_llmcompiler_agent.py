from llama_hub.tools.database import DatabaseToolSpec
from llm_compiler_agent_pack.base import LLMCompilerAgentPack

db_tools = DatabaseToolSpec(uri="sqlite:///files//database//employees.db")
agent = LLMCompilerAgentPack(db_tools.to_tool_list())

response = agent.run(
    "List the HR department employee "
    "with the highest salary "
)
