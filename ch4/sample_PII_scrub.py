from llama_index.postprocessor import  NERPIINodePostprocessor
from llama_index.llms import HuggingFaceLLM
from llama_index.schema import NodeWithScore, TextNode
from llama_index import ServiceContext

original = """Dear Jane Doe. Your address has been recorded in our database. \
Please confirm it is valid: 8804 Vista Serro Dr. Cabo Robles, California(CA)."""

node = TextNode(text=original)
service_context = ServiceContext.from_defaults()
processor = NERPIINodePostprocessor(service_context=service_context)
clean_nodes = processor.postprocess_nodes([NodeWithScore(node=node)])

print(clean_nodes[0].node.get_text())
