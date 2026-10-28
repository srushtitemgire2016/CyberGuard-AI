from pathlib import Path

DOCUMENTS_FOLDER = Path("documents")


def load_documents():
    documents = []

    for file_path in DOCUMENTS_FOLDER.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".txt", ".md"]:
            try:
                content = file_path.read_text(encoding="utf-8").strip()

                if content:
                    documents.append({
                        "filename": file_path.name,
                        "content": content
                    })

            except (OSError, UnicodeError) as error:
                print(f"Could not read {file_path.name}: {error}")

    return documents


if __name__ == "__main__":
    loaded_documents = load_documents()

    print(f"Documents loaded: {len(loaded_documents)}")

    for document in loaded_documents:
        print(f"\n--- {document['filename']} ---")
        print(document["content"])