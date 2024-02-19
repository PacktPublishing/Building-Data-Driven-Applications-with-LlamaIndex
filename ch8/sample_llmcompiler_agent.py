from llama_index.tools.database import DatabaseToolSpec
from llama_index.packs.agents_llm_compiler import LLMCompilerAgentPack

db_tools = DatabaseToolSpec(uri="sqlite:///files//database//employees.db")
agent = LLMCompilerAgentPack(db_tools.to_tool_list())

response = agent.run(
    "List the HR department employee "
    "with the highest salary "
)

# am schimbat doar importul . nu mai e necesar download-ul inainte
# de mentionat: pip install llama-index-packs-agents-llm-compiler