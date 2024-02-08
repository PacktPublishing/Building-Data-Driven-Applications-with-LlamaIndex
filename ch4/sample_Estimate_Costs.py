from llama_index import ServiceContext
from llama_index.llms import MockLLM
from llama_index.schema import TextNode
from llama_index.callbacks import CallbackManager, TokenCountingHandler
from llama_index.extractors import QuestionsAnsweredExtractor

llm = MockLLM(max_tokens=256)
token_counter = TokenCountingHandler(verbose=False)

callback_manager = CallbackManager([token_counter])
service_context = ServiceContext.from_defaults(
    callback_manager=callback_manager,
    llm=llm
)

sample_text = "LlamaIndex is a powerful tool used to create efficient indices from data."
extractor = QuestionsAnsweredExtractor(
    service_context=service_context, 
    llm=llm, 
    show_progress=False
)

Questions_metadata = extractor.extract([TextNode(text=sample_text)])

print(f"LLM Prompt Tokens: {token_counter.prompt_llm_token_count}")
print(f"LLM Completion Tokens: {token_counter.completion_llm_token_count}")
print(f"Total LLM Token Count: {token_counter.total_llm_token_count}")
