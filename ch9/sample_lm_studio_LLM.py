from llama_index.llms.openai import OpenAI
llm = OpenAI(
    api_base='http://localhost:1234/v1', 
    temperature=0.7
)
print(llm.complete('Who is Lionel Messi?'))
