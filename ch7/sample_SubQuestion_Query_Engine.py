from llama_index.tools.query_engine import QueryEngineTool
from llama_index.query_engine.router_query_engine import RouterQueryEngine
from llama_index.query_engine import SubQuestionQueryEngine
from llama_index.selectors.pydantic_selectors import PydanticMultiSelector
from llama_index import SummaryIndex, SimpleDirectoryReader
from llama_index.extractors import TitleExtractor  

documents = SimpleDirectoryReader("files/sample").load_data()
title_extractor = TitleExtractor()
for doc in documents:
    title_metadata = title_extractor.extract([doc])
    doc.metadata.update(title_metadata[0])

indexes = []
query_engines = []
tools = []

for doc in documents:
    document_title = doc.metadata['document_title']
    file_name = doc.metadata['file_name']
    index = SummaryIndex.from_documents([doc])
    query_engine = index.as_query_engine(
        response_mode="tree_summarize",
        use_async=True,
    )
    tool = QueryEngineTool.from_defaults(
        query_engine=query_engine,
        name=file_name,
        description=f"Contains data about {document_title}",
    )
    indexes.append(index)
    query_engines.append(query_engine)
    tools.append(tool)

from llama_index.callbacks import CallbackManager, LlamaDebugHandler
from llama_index import ServiceContext
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(
    callback_manager=callback_manager
)

qe = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=tools,
    service_context=service_context,
    use_async=True
)

response = qe.query(
"Compare buildings from ancient Athens and ancient Rome"
)
print(response)
