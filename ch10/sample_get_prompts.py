from llama_index.core import SummaryIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("files").load_data()
summary_index = SummaryIndex.from_documents(documents)
qe = summary_index.as_query_engine()

prompts = qe.get_prompts()

for k, p in prompts.items():
    print(f"Prompt Key: {k}")
    print("Text:")
    print(p.get_template())
    print("\n")
