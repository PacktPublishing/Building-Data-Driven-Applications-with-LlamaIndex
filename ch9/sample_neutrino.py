from llama_index.core.llms import ChatMessage
from llama_index.llms.neutrino import Neutrino

llm = Neutrino(
    api_key="<your-Neutrino_API_key>",
    router="<Neutrino-router_ID>"
)

while True:
    user_message = input("Ask a question: ")
    if user_message.lower() == 'exit':
        print("Exiting chat...")
        break
    response = llm.complete(user_message)
    print(f"LLM answer: {response}")
    print(f"Answered by: {response.raw['model']}")
    
    
'''
To globally configure the llm, use Settings like this:

from llama_index.core import Settings
Settings.llm = llm
'''