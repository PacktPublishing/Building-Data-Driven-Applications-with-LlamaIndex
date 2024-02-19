from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.schema import TextNode, NodeWithScore

nodes = [
    TextNode(
        text="Article 1", 
        metadata={"summary": "Summary of article 1"}
    ),
    TextNode(
        text="Article 2", 
        metadata={"summary": "Summary of article 2"}
    ),
]

node_with_score_list = [
    NodeWithScore(node=node) for node in nodes
]
pp = MetadataReplacementPostProcessor(
    target_metadata_key="summary"
)
processed_nodes = pp.postprocess_nodes(
    node_with_score_list
)
for node_with_score in processed_nodes:
    print(f"Replaced Text: {node_with_score.node.text}")
