
import tiktoken
from llama_index import TreeIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import MockLLM
from llama_index.callbacks import CallbackManager, TokenCountingHandler

llm = MockLLM(max_tokens=256)
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
callback_manager = CallbackManager([token_counter])
service_context = ServiceContext.from_defaults(
    callback_manager=callback_manager,
    llm=llm
)

documents = SimpleDirectoryReader("cost_prediction_samples").load_data()

index = TreeIndex.from_documents(
    documents=documents,
    service_context=service_context, 
    num_children=2,
    llm=llm, 
    show_progress=True)
print("Total LLM Token Count:", token_counter.total_llm_token_count)
