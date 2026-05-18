# 🔐 CyberSecure AI Assistant

A production-ready **cybersecurity-only AI chatbot** built with Streamlit and the Anthropic Claude API. The assistant exclusively answers questions about cybersecurity, SOC operations, ethical hacking, SIEM tools, threat detection, malware analysis, and AI in security.

---

## 📁 Folder Structure

```
cybersec_chatbot/
├── app.py                        # Main Streamlit application
├── utils.py                      # API client, chat helpers, export functions
├── prompt_guard.py               # Topic validation & prompt injection protection
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── .streamlit/
│   ├── config.toml               # Streamlit theme & server config
│   └── secrets.toml.example      # Secrets template (for Streamlit Cloud)
└── README.md                     # This file
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🤖 AI Responses | Powered by Anthropic Claude (claude-sonnet-4) |
| 🛡️ Topic Guard | Double-layer filtering: regex keyword match + hardened system prompt |
| ⛔ Injection Protection | 12+ prompt injection / jailbreak patterns blocked |
| 💬 Chat History | Full session memory with timestamps |
| ⬇️ Export | Download chat as JSON or plain-text transcript |
| 🎨 Cyberpunk UI | Dark navy, neon cyan/green, scanline overlay, animated header |
| 📋 Sample Questions | 12 pre-built sample queries in the sidebar |
| 📊 Stats | Live counter for total vs blocked queries |
| 🚀 Cloud-Ready | Works on Streamlit Cloud, Render, Hugging Face Spaces |

---

## 🚀 Local Installation

### Prerequisites

- Python 3.9 or higher
- An [Anthropic API key](https://console.anthropic.com/)

### Step 1 — Clone / download the project

```bash
git clone <your-repo-url>
cd cybersec_chatbot
```

### Step 2 — Create a virtual environment (recommended)

```bash
python -m venv venv

# Activate (Linux / macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure your API key

```bash
cp .env.example .env
```

Edit `.env` and replace `your_anthropic_api_key_here` with your real key:

```
ANTHROPIC_API_KEY=sk-ant-api03-...
```

> The app loads `.env` automatically via `python-dotenv` — **never commit this file**.

### Step 5 — Run the application

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**.

---

## ☁️ Deployment

### Streamlit Cloud

1. Push the project to a **public or private GitHub repo**.
2. Go to [share.streamlit.io](https://share.streamlit.io) → New App.
3. Select your repo, branch, and `app.py` as the entry point.
4. Under **Advanced Settings → Secrets**, add:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-..."
   ```
5. Click **Deploy**. Done.

### Render

1. Create a new **Web Service** on [render.com](https://render.com).
2. Connect your GitHub repo.
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Add `ANTHROPIC_API_KEY` as an Environment Variable.
5. Deploy.

### Hugging Face Spaces

1. Create a new **Space** (SDK: Streamlit).
2. Upload all files (or connect via Git).
3. Add `ANTHROPIC_API_KEY` in **Settings → Repository secrets**.
4. The Space will build and launch automatically.

---

## 🔒 Security Notes

- **API keys** are loaded from environment variables — never hard-coded.
- **Prompt injection** patterns are detected and blocked *before* the LLM is called.
- **Topic restriction** is enforced at two levels: client-side keyword filtering and a hardened system prompt that the model is instructed to follow strictly.
- **Session isolation**: all state lives in `st.session_state`; no data persists between browser sessions.

---

## 🗂️ Architecture Overview

```
User Input
    │
    ▼
prompt_guard.validate_prompt()
    ├── Injection detected? ──► Block + warn user
    ├── Off-topic?          ──► Block + redirect user
    │
    ▼ (valid cybersec query)
utils.get_ai_response()
    ├── build_api_history()  ──► format messages for API
    ├── build_system_prompt() ─► hardened system instructions
    └── anthropic.messages.create() ──► Claude API
    │
    ▼
Render response bubble in Streamlit
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `anthropic` | Official Anthropic Python SDK |
| `python-dotenv` | Load `.env` file for local development |

---

## 🤝 Contributing

PRs welcome! Please keep all contributions scoped to cybersecurity tooling, UI improvements, or security hardening.

---

*Built with ❤️ for the security community.*
