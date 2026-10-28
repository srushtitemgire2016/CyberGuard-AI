from document_loader import load_documents


def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_documents()

    for document in documents:
        chunks = split_text(document["content"])

        print(f"\nDocument: {document['filename']}")
        print(f"Total chunks: {len(chunks)}")

        for index, chunk in enumerate(chunks, start=1):
            print(f"\n--- Chunk {index} ---")
            print(chunk)