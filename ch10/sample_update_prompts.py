from llama_index.core import SummaryIndex, SimpleDirectoryReader
from llama_index.core import PromptTemplate

documents = SimpleDirectoryReader("files").load_data()
summary_index = SummaryIndex.from_documents(documents)
qe = summary_index.as_query_engine()
print(qe.query("Who burned Rome?"))
print("------------------------")

new_qa_template = (
"Context information is below."
"---------------------"
"{context_str}"
"---------------------"
"Given the context information "
"and any of your prior knowledge, "
"answer the query."
"Query: {query_str}"
"Answer:")

template = PromptTemplate(new_qa_template)

qe.update_prompts(
    {"response_synthesizer:text_qa_template": template}
)
print(qe.query("Who burned Rome?"))