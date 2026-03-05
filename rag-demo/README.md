# 🤖 Vertex AI RAG Agent (Python ADK)

This project implements a Retrieval-Augmented Generation (RAG) system using the Google Agent Development Kit (ADK) and Vertex AI. It is managed with **uv** for high-performance dependency resolution.

## 📁 Project Structure

```text
rag-demo
├── data
│   └── file.pdf  # Your source documents
├── pyproject.toml                             # uv project config
├── README.md
├── scripts
│   ├── ingest_docs.py                         # Phase 2: Upload files
│   ├── list_corpora.py                        # Utility: View all corpora
│   ├── list_files.py                          # Utility: View uploaded files
│   └── setup_rag.py                           # Phase 1: Create infrastructure
├── src
│   └── my_agent
│       └── agent.py                           # Phase 3: The Agent logic
└── uv.lock                                    # Locked dependencies

```

---

## 🏗️ Workflow Phases

### Phase 1: Infrastructure Setup

* **Action:** `uv run python scripts/setup_rag.py`
* **Goal:** Create the `RagCorpus` in Vertex AI and obtain your `RAG_CORPUS_ID`.

### Phase 2: Data Ingestion

* **Action:** `uv run python scripts/ingest_docs.py`
* **Goal:** Process and index the PDF located in the `/data` folder.

### Phase 3: Interaction & Generation

* **Action:** `uv run python src/my_agent/agent.py`
* **Goal:** Chat with the "Azure in a Month of Lunches" PDF using Gemini 2.5 Flash.

---

## 🔍 Management Utilities

| Script | Command |
| --- | --- |
| **List Corpora** | `uv run python scripts/list_corpora.py` |
| **List Indexed Files** | `uv run python scripts/list_files.py` |

---

## 🚦 Setup

1. **Initialize Project:**
```bash
uv sync

```


2. **Environment Variables:**
Create a `.env` file in the root:
```env
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="us-central1"
RAG_CORPUS_ID="your-id-from-phase-1"

```


3. **Running via ADK Web UI:**
To test the agent in a visual browser interface:
```bash
uv run adk web src.my_agent:rag_app

```