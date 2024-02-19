from llama_index.core import Document
from llama_index.core.schema import (
    TextNode, 
    NodeRelationship, 
    RelatedNodeInfo
)
doc = Document(text="First sentence. Second Sentence")
n1 = TextNode(text="First sentence", node_id=doc.doc_id)
n2 = TextNode(text="Second sentence", node_id=doc.doc_id)

n1.relationships[NodeRelationship.NEXT] = n2.node_id 
n2.relationships[NodeRelationship.PREVIOUS] = n1.node_id
print(n1.relationships)
print(n2.relationships)

