import asyncio
from llama_index.core import KeywordTableIndex
from llama_index.core import SimpleDirectoryReader

async def retrieve(retriever, query, label):
    response = await retriever.aretrieve(query)
    print(f"{label} retrieved {str(len(response))} nodes")

async def main():
    reader = SimpleDirectoryReader('files')
    documents = reader.load_data()
    index = KeywordTableIndex.from_documents(documents)
    retriever1 = index.as_retriever(
retriever_mode='default'
)
    retriever2 = index.as_retriever(
retriever_mode='simple'
)
    query = "Where is the Colosseum?"

    await asyncio.gather(
        retrieve(retriever1, query, '<llm>'),
        retrieve(retriever2, query, '<simple>')
    )
asyncio.run(main())
