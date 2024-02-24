from llama_index.core.selectors import LLMSingleSelector
options = [
    "option 1 this is good for summarization questions",
    "option 2: this is useful for precise definitions",
    "option 3: this is useful for comparing concepts",
]
selector = LLMSingleSelector.from_defaults()

decision = selector.select(
    options, 
    query="What's the definition of space?"
).selections[0]
print(decision.index+1)
print(decision.reason)