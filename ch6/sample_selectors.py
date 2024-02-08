from llama_index.selectors.llm_selectors import LLMSingleSelector
options = [
    "option 1: this is good for summarization questions",
    "option 2: this is useful for precise definitions",
    "option 3: this is useful for comparing concepts",
]
selector = LLMSingleSelector.from_defaults()

decision = selector.select(
    options, 
    query="What's the definition of gravity?"
).selections[0]
print(decision.index)
print(decision.reason)
