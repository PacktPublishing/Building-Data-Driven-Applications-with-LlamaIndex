import tiktoken
from llama_index.core import MockEmbedding, VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.core.llms.mock import MockLLM

embed_model = MockEmbedding(embed_dim=1536)
llm = MockLLM(max_tokens=256)
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
callback_manager = CallbackManager([token_counter])

Settings.embed_model=embed_model
Settings.llm=llm
Settings.callback_manager=callback_manager

documents = SimpleDirectoryReader("cost_prediction_samples").load_data()
index = VectorStoreIndex.from_documents(
    documents=documents,
    show_progress=True)
print("Embedding Token Count:", token_counter.total_embedding_token_count)

query_engine = index.as_query_engine()  
response = query_engine.query("What's the cat's name?")   
print("Query LLM Token Count:", token_counter.total_llm_token_count)
print("Query Embedding Token Count:",token_counter.total_embedding_token_count)

