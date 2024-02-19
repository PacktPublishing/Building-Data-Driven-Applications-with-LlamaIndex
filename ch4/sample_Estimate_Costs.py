from llama_index.core import Settings
from llama_index.core.extractors import QuestionsAnsweredExtractor
from llama_index.core.llms.mock import MockLLM
from llama_index.core.schema import TextNode
from llama_index.core.callbacks import (
    CallbackManager, 
    TokenCountingHandler
)

llm = MockLLM(max_tokens=256)
counter = TokenCountingHandler(verbose=False)
callback_manager = CallbackManager([counter])

Settings.llm = llm
Settings.callback_manager = CallbackManager([counter])

sample_text = (
    "LlamaIndex is a powerful tool used "
    "to create efficient indices from data."
)
nodes= [TextNode(text=sample_text)]

extractor = QuestionsAnsweredExtractor(
    show_progress=False
)

Questions_metadata = extractor.extract(nodes)

print(f"Prompt Tokens: {counter.prompt_llm_token_count}")
print(f"Completion Tokens: {counter.completion_llm_token_count}")
print(f"Total Token Count: {counter.total_llm_token_count}")
