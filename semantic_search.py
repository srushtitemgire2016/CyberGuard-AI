from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from text_splitter import split_text
from document_loader import load_documents


# Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def build_search_index():
    documents = load_documents()

    chunks = []
    metadata = []

    for document in documents:
        document_chunks = split_text(document["content"])

        for chunk in document_chunks:
            chunks.append(chunk)
            metadata.append(document["filename"])

    if not chunks:
        return None, [], []

    # Convert text chunks into numerical embeddings
    embeddings = model.encode(chunks, convert_to_numpy=True)

    # Normalize vectors for cosine similarity search
    embeddings = embeddings.astype("float32")
    faiss.normalize_L2(embeddings)

    # Create the FAISS index
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks, metadata


def search_documents(question, index, chunks, metadata, top_k=3):
    if index is None:
        return []

    # Convert the question into an embedding
    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    faiss.normalize_L2(question_embedding)

    # Search for the most similar chunks
    number_of_results = min(top_k, len(chunks))
    scores, indices = index.search(
        question_embedding,
        number_of_results
    )

    results = []

    for score, position in zip(scores[0], indices[0]):
        if position >= 0:
            results.append({
                "filename": metadata[position],
                "content": chunks[position],
                "score": float(score)
            })

    return results


if __name__ == "__main__":
    index, chunks, metadata = build_search_index()

    if index is None:
        print("No documents found to search.")
    else:
        question = input("\nEnter your cybersecurity question: ")

        results = search_documents(
            question,
            index,
            chunks,
            metadata
        )

        print("\nRelevant information:")

        for result in results:
            print(f"\nSource: {result['filename']}")
            print(f"Similarity score: {result['score']:.3f}")
            print(result["content"])