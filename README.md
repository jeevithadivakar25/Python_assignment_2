# AI API Integration Project

**Course:** Generative AI
**Institution:** East West Institute of Technology (EWIT)
**Student:** Jeevitha Divakar
**Mentor:** Jacob Dennis
**Date:** March 2026

---

## 1. Project Description

This project demonstrates the integration of six major Generative AI platforms into a Python-based development environment. Each script is designed to take a user prompt, query a specific AI model via its API, handle errors gracefully, and return the generated text.

As of March 2026, this project specifically addresses and resolves several industry-wide API migrations:

- **Hugging Face:** Transitioned to the `router.huggingface.co` endpoint.
- **Google Gemini:** Migrated from `generativeai` to the modern `google-genai` SDK.
- **Groq:** Updated to `Llama 3.1` models following the decommissioning of legacy Llama 3 versions.
- **OpenAI:** Implemented with quota-handling logic.

---

## 2. Setup Instructions

Ensure you have **Python 3.10+** installed, then follow these steps:

### Step 1 — Create a Virtual Environment

```bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate
```

### Step 2 — Install Dependencies

```bash
pip install openai groq requests google-genai cohere python-dotenv
```

### Step 3 — Configure Environment Variables

Create a file named `.env` in the root directory and add your API keys:

```plaintext
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_token
GOOGLE_API_KEY=your_key
COHERE_API_KEY=your_key
```

---

## 3. How to Obtain API Keys

| Provider | Where to Get the Key |
|---|---|
| OpenAI | [platform.openai.com](https://platform.openai.com) |
| Groq | [console.groq.com](https://console.groq.com) |
| Ollama (Local) | No key required — download at [ollama.ai](https://ollama.ai) |
| Hugging Face | Create a "Read" token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| Google Gemini | Obtain from [aistudio.google.com](https://aistudio.google.com) |
| Cohere | Get your key at [dashboard.cohere.com](https://dashboard.cohere.com) |

---

## 4. How to Run Each Program

Each script can be run individually from the terminal:

```bash
python openai_api.py        # OpenAI
python groq_api.py          # Groq
python ollama_api.py        # Ollama (ensure the Ollama app is running first)
python huggingface_api.py   # Hugging Face
python gemini_api.py        # Google Gemini
python cohere_api.py        # Cohere
python multi_api_query.py   # Bonus: Unified multi-provider query
```

---

## 5. Screenshots of Working Programs

All screenshots are located in the `/screenshots` folder.

| Provider | File Name | Status |
|---|---|---|
| Google Gemini | `gemini_output.png` | ✅ Working (Gemini 2.5 Flash) |
| Groq | `groq_output.png` | ✅ Working (Llama 3.1 8B) |
| Hugging Face | `hf_output.png` | ✅ Working (Qwen 2.5 via Router) |
| Cohere | `cohere_output.png` | ✅ Working (Command A 2025) |
| Ollama | `ollama_output.png` | ✅ Working (Local Llama 3) |
| OpenAI | `openai_output.png` | ✅ Script Validated (Quota 429 Captured) |

---

## 6. Project Structure

```
ai_api_integration/
├── venv/                   # Virtual environment (not in Git)
├── screenshots/            # Output images for each API
├── .env                    # Private API keys (not in Git)
├── .gitignore              # Ignores venv and .env
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── [provider]_api.py       # Individual provider scripts
```
