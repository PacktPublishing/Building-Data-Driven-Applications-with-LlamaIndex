from llama_index.core import DocumentSummaryIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("files").load_data()
index = DocumentSummaryIndex.from_documents(
    documents, 
    show_progress=True
)

summary1 = index.get_document_summary(documents[0].doc_id)
summary2 = index.get_document_summary(documents[1].doc_id)
print("\nSummary of the first document:" + summary1)
print("\nSummary of the second document:" + summary2)