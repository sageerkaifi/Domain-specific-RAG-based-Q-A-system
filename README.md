Of course 👍 Let’s draft a **README.md** for your current **RAG-based Political Science Q\&A system**. I’ll keep it professional and resume/portfolio-friendly.

---

# 📘 Retrieval-Augmented Generation (RAG) for Political Science Q\&A

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system to answer **Political Science & Indian Polity questions**.
It combines:

* **Document retrieval** (Chroma vector database + embeddings)
* **Large Language Model (LLM)** (Hugging Face model for generation)

The system ingests **Indian Polity PDFs**, chunks and embeds them, stores in **ChromaDB**, and then retrieves the most relevant context to answer user queries in a professor-like manner.

---

## ✨ Features

* 📄 **Multi-PDF ingestion** → Load multiple textbooks / PDFs.
* 🧩 **Document chunking** → Splits into overlapping chunks for better retrieval.
* 🔍 **Vector search** → Stores embeddings in **Chroma** for semantic search.
* 🤖 **LLM-powered Q\&A** → Uses Hugging Face models (e.g., `flan-t5-small`).
* 📊 **Metadata tracking** → Stores filename + timestamp for each chunk.
* ⚡ **Batch insertion** → Prevents exceeding Chroma batch limits.
* 🔁 **RAG pipeline** → Retrieval + Generation for accurate, context-grounded answers.

---

## 🏗️ Architecture

1. **PDF Loader** → Reads Indian Polity (or other) textbooks.
2. **Text Splitter** → Splits into 1000-char chunks with overlap.
3. **Embedding Generator** → Uses `sentence-transformers/all-MiniLM-L6-v2`.
4. **Chroma Vector DB** → Stores and retrieves embeddings.
5. **Retriever** → Finds top-5 relevant chunks for a query.
6. **LLM (Generator)** → Hugging Face `flan-t5-small` answers using retrieved context.

```
[PDFs] → [Text Splitter] → [Embeddings] → [ChromaDB]
                                      ↓
                             [Retriever + LLM]
                                      ↓
                               [Final Answer]
```

---

## ⚙️ Installation

Run in **local** with Python 3.9+.

```bash
pip install langchain langchain-huggingface langchain-chroma transformers pypdf
```

---

## 🚀 Usage

### 1. Add PDFs


### 2. Build Vector DB

```python
from embeddedvector import retriver
```

This:

* Loads all PDFs from `./pdfs/`
* Splits → Embeds → Stores in `chroma_langchain_db/`

### 3. Ask Questions

```python
from main_rag import chain, retriver

query = "What are Fundamental Rights?"
context = retriver.invoke(query)
result = chain.invoke({"context": context, "query": query})

print(result)
```

---

## 📊 Evaluation

we can evaluate using:

* **Human Evaluation** (clarity, completeness, relevance).



## 🔮 Future Work

* ✅ Add **Streamlit UI** for interactive use.
* ✅ Deploy on **Hugging Face Spaces**.
* ✅ Integrate **Ragas evaluation pipeline**.
* ✅ Experiment with larger models (`flan-t5-base`, `llama-2-7b`).

---

## 👨‍💻 Author

Developed by **Sagheer Kaifi**
MCA Final Semester | Data Science & NLP Enthusiast


