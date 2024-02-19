from llama_index.question_gen.openai import OpenAIQuestionGenerator
from llama_index.core.tools import RetrieverTool, ToolMetadata
from llama_index.core import VectorStoreIndex, SummaryIndex, SimpleDirectoryReader, QueryBundle

documents = SimpleDirectoryReader("files").load_data()
vector_index = VectorStoreIndex.from_documents([documents[0]])
summary_index = SummaryIndex.from_documents([documents[1]])

vector_tool_metadata = ToolMetadata(
    name="Vector Tool", 
    description="Use this for answering questions about Ancient Rome"
)
summary_tool_metadata = ToolMetadata(
    name="Summary Tool", 
    description="Use this for answering questions about dogs"
)

vector_tool = RetrieverTool(
    retriever=vector_index.as_retriever(), 
    metadata=vector_tool_metadata
)
summary_tool = RetrieverTool(
    retriever=summary_index.as_retriever(), 
    metadata=summary_tool_metadata
)

question_generator = OpenAIQuestionGenerator.from_defaults()
query_bundle = QueryBundle(query_str="Tell me about dogs and Ancient Rome")
sub_questions = question_generator.generate(
    tools=[vector_tool.metadata, summary_tool.metadata], 
    query=query_bundle
)

for sub_question in sub_questions:
    print(f"{sub_question.tool_name}: {sub_question.sub_question}")
