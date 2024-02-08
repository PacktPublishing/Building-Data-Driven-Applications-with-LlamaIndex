from llama_index.indices.query.query_transform import DecomposeQueryTransform
decompose = DecomposeQueryTransform()
query_bundle = decompose.run(
"Tell me about buildings in ancient Rome"
)
print(query_bundle.query_str)
