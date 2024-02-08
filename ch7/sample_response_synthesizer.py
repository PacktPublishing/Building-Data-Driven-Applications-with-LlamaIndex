from llama_index.schema import Node, NodeWithScore 
from llama_index import get_response_synthesizer 

nodes = [ 
    Node(text="The town square clock was built in 1895"), 
    Node(text="A turquoise parrot lives in the Amazon"), 
    Node(text="A rare orchid blooms only at midnight"), 
] 

node_with_score_list = [NodeWithScore(node=node) for node in nodes] 
synth = get_response_synthesizer( 
    response_mode="refine", 
    use_async=False, 
    streaming=False, 
) 

response = synth.synthesize( 
    "When was the clock built?", 
    nodes=node_with_score_list 
) 
print(response) 