from llama_index.core.agent import AgentRunner
from llama_index.agent.openai import OpenAIAgentWorker
from llama_index.tools.database import DatabaseToolSpec

db_tools = DatabaseToolSpec(uri="sqlite:///files//database//employees.db")
tools = db_tools.to_tool_list()

step_engine = OpenAIAgentWorker.from_tools(
    tools,
    verbose=True
)

agent = AgentRunner(step_engine)
input =  (
    "Find the highest paid HR employee and write "
    "them an email announcing a bonus"
)

task = agent.create_task(input)
step_output = agent.run_step(task.task_id)

while not step_output.is_last:
    step_output = agent.run_step(task.task_id)

response = agent.finalize_response(task.task_id)
print(response)
