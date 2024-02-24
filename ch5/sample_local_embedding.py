from llama_index.embeddings.huggingface import HuggingFaceEmbedding
embedding_model = HuggingFaceEmbedding(
    model_name="WhereIsAI/UAE-Large-V1"
)
embeddings = embedding_model.get_text_embedding(
    "The quick brown fox jumps over the lazy cat!"
)
print(embeddings[:15]) 

