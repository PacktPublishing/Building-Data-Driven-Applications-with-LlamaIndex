from llama_index.core.postprocessor import NERPIINodePostprocessor
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.schema import NodeWithScore, TextNode

original = (
    "Dear Jane Doe. Your address has been recorded in "
    "our database. Please confirm it is valid: 8804 Vista "
    "Serro Dr. Cabo Robles, California(CA)."
)

node = TextNode(text=original)
processor = NERPIINodePostprocessor()

clean_nodes = processor.postprocess_nodes(
    [NodeWithScore(node=node)]
)

print(clean_nodes[0].node.get_text())

