# 🛡️ CyberGuard AI — Cybersecurity Knowledge Assistant

An AI-powered cybersecurity knowledge assistant that helps users understand cyber threats, security vulnerabilities, and prevention techniques through a conversational interface.

CyberGuard AI combines Flask, Retrieval-Augmented Generation (RAG), semantic search, and Google's Gemini API to provide answers grounded in a cybersecurity knowledge base.

## ✨ Features

- **AI-Powered Assistance:** Ask questions about cybersecurity in natural language.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from local cybersecurity documents before generating an answer.
- **Semantic Search:** Uses sentence embeddings and FAISS to find relevant document passages.
- **Cybersecurity Knowledge Base:** Includes information about phishing, malware, ransomware, SQL injection, XSS, DDoS, password attacks, network security, cryptography, and more.
- **Web Interface:** Interactive interface built with Flask, HTML, CSS, and JavaScript.
- **Source-Based Responses:** Uses retrieved knowledge to help ground AI-generated answers.
- **Modular Architecture:** Separates document loading, text splitting, semantic search, and web application logic.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web application and routing |
| Google Gemini API | AI-generated responses |
| Sentence Transformers | Text embeddings |
| FAISS | Similarity search over document embeddings |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend interactions |
| Git and GitHub | Version control and project hosting |

## 🏗️ How It Works

1. **Document Loading:** Reads supported cybersecurity knowledge files from the `documents/` directory.
2. **Text Splitting:** Divides documents into smaller chunks for retrieval.
3. **Embedding Generation:** Converts the chunks into numerical vector representations using a sentence-transformer model.
4. **Semantic Search:** Uses FAISS to retrieve passages relevant to the user's question.
5. **Answer Generation:** Sends the question and retrieved context to the Gemini API.
6. **Response Display:** Returns the generated answer through the web interface.

## 📂 Project Structure

```text
Cyberguard_AI/
├── app.py
├── document_loader.py
├── text_splitter.py
├── semantic_search.py
├── requirement.txt
├── documents/
│   ├── phishing.txt
│   ├── malware.txt
│   ├── ransomware.txt
│   ├── sql_injection.txt
│   └── ... other cybersecurity documents
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── assistant.html
│   ├── library.html
│   └── vulnerabilities.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11 or a compatible Python version supported by the project's dependencies
- Git
- A Google Gemini API key
- Internet access for the Gemini API and initial model downloads

### 1. Clone the repository

```bash
git clone https://github.com/srushtitemgire2016/CyberGuard-AI.git
cd CyberGuard-AI
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the application using the virtual environment's Python executable directly instead.

### 3. Install dependencies

```bash
python -m pip install -r requirement.txt
```

### 4. Configure the Gemini API key

Set the API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY = Read-Host "Paste your Gemini API key"
```

Obtain an API key through [Google AI Studio](https://aistudio.google.com/apikey).

Keep the key private. Never commit it to GitHub.

### 5. Run the application

```powershell
python app.py
```

Open the local address displayed by Flask, usually:

```text
http://127.0.0.1:5000
```

Keep the terminal running while using the application.

## 🔐 Security and Limitations

- CyberGuard AI is an educational cybersecurity information assistant, not a replacement for professional incident-response services.
- Answers depend on the available knowledge documents, retrieved context, and AI model output.
- AI-generated responses may be incomplete or inaccurate. Verify important security decisions using trusted sources.
- Never enter passwords, API keys, or other sensitive credentials into the assistant.
- Do not upload API keys, `.env` files, or virtual-environment folders to GitHub.
- The Flask development server is intended for local development, not production deployment.

## 🚀 Future Improvements

- Add more cybersecurity knowledge sources.