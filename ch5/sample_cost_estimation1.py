import tiktoken
from llama_index.core import TreeIndex, SimpleDirectoryReader, Settings
from llama_index.core.llms.mock import MockLLM
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler

llm = MockLLM(max_tokens=256)
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
callback_manager = CallbackManager([token_counter])

Settings.callback_manager=callback_manager
Settings.llm=llm

documents = SimpleDirectoryReader("cost_prediction_samples").load_data()

index = TreeIndex.from_documents(
    documents=documents,
    num_children=2,
    show_progress=True)

print("Total LLM Token Count:", token_counter.total_llm_token_count)


