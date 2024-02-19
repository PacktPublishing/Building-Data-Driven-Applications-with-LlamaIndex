from llama_index.tools.database import DatabaseToolSpec
from llama_index.core.tools import FunctionTool
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI

def write_text_to_file(text, filename):
    """
    Writes the text to a file with the specified filename.
    Args:
        text (str): The text to be written to the file.
        filename (str): File name to write the text into.
    Returns: None
    """
    with open(filename, 'w') as file:
        file.write(text)
        
save_tool = FunctionTool.from_defaults(fn=write_text_to_file)
db_tools = DatabaseToolSpec(uri="sqlite:///files//database//employees.db")
tools = [save_tool]+db_tools.to_tool_list()

llm = OpenAI(model="gpt-4")
agent = OpenAIAgent.from_tools(
    tools=tools, 
    llm=llm, 
    verbose=True,
    max_function_calls=20
)

response = agent.chat(
    "For each IT department employee with a salary lower "
    "than the average organization salary, write an email,"
    "announcing a 10% raise and then save all emails into "
    "a file called 'emails.txt'")
print(response)
