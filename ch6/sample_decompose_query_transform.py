from llama_index.core.indices.query.query_transform.base import DecomposeQueryTransform
decompose = DecomposeQueryTransform()
query_bundle = decompose.run(
    "Tell me about buildings in ancient Rome"
)
print(query_bundle.query_str)
