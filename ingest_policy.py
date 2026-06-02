# ingest_policy.py

import os

from app.rag.pdf_loader import (
    load_pdf
)

from app.rag.chunker import (
    chunk_text
)

from app.rag.embedder import (
    create_embeddings
)

from app.rag.vector_store import (
    store_chunks
)

DATA_FOLDER = "data"

pdf_files = [

    file

    for file in os.listdir(
        DATA_FOLDER
    )

    if file.lower().endswith(
        ".pdf"
    )

]

print(
    f"\nFound {len(pdf_files)} PDF(s)"
)

for pdf_file in pdf_files:

    pdf_path = os.path.join(
        DATA_FOLDER,
        pdf_file
    )

    print(
        f"\nProcessing: {pdf_file}"
    )

    text = load_pdf(
        pdf_path
    )

    chunks = chunk_text(
        text
    )

    embeddings = create_embeddings(
        chunks
    )

    store_chunks(
        chunks,
        embeddings
    )

    print(
        f"Indexed: {pdf_file}"
    )

print(
    "\nAll PDFs Indexed Successfully"
)