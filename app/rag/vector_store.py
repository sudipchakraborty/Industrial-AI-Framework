# app/rag/vector_store.py

import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_or_create_collection(
    "hr_policies"
)


def store_chunks(
    chunks,
    embeddings
):

    ids = [

        str(uuid.uuid4())

        for _ in chunks

    ]

    collection.add(

        ids=ids,

        documents=chunks,

        embeddings=embeddings.tolist()

    )