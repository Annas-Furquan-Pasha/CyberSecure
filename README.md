# 🔐 CyberSecure AI Assistant

An AI-powered cybersecurity chatbot built with Streamlit and Groq LLMs.

CyberSecure AI is a domain-restricted assistant that only responds to cybersecurity-related questions such as:
- SOC operations
- SIEM tools
- Malware analysis
- Threat hunting
- Ethical hacking
- Incident response
- AI in cybersecurity

The chatbot includes prompt injection protection, topic validation, WhatsApp-style chat UI, and secure API handling.

---

# 🚀 Features

- 🔒 Cybersecurity-only AI assistant
- 🛡️ Prompt injection & jailbreak protection
- 🤖 Powered by Groq + Llama 3.3
- 💬 WhatsApp-style modern chat interface
- 📊 Query & blocked request tracking
- ⛔ Off-topic question rejection
- 📁 Export chat history (JSON/TXT)
- ⚡ Fast Groq inference
- 🎨 Cyberpunk-themed Streamlit UI
- 🧩 Modular architecture (`app.py`, `ui.py`, `utils.py`)
- ⏱️ Basic rate limiting protection
- 🔐 Environment variable API security

---

# 🖼️ Screenshots

## Homepage


```text
assets/home-page.png
```

## Chat Example

```text
assets/chat-demo.png
```

---

# 🏗️ Project Structure

```bash
CyberSecureAI/
│
├── app.py                 # Main application logic
├── ui.py                  # UI rendering & styling
├── utils.py               # Groq API + helper functions
├── prompt_guard.py        # Prompt validation & security
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── assets/
    ├── homepage.png
    └── chat-demo.png
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Annas-Furquan-Pasha/CyberSecure.git

cd CyberSecure
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\\Scripts\\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application will run at:

```text
http://localhost:8501
```

---

# 🧠 Architecture

```text
User Input
    ↓
Prompt Guard
    ↓
Greeting Detection
    ↓
Cybersecurity Validation
    ↓
Groq API (Llama 3.3)
    ↓
Response Rendering
```

---

# 🛡️ Security Features

## Prompt Injection Protection

The chatbot blocks:
- Jailbreak attempts
- System prompt extraction
- Role override attacks
- “Ignore previous instructions” prompts

---

## Topic Restriction

Only cybersecurity-related queries are allowed.

Examples:
- SIEM
- SOC
- Malware
- Threat Intelligence
- Ethical Hacking
- AI Security

Off-topic requests are politely rejected.

---

## Rate Limiting

Basic cooldown protection prevents API spam requests.

---

# 🤖 Tech Stack

| Technology | Usage |
|---|---|
| Streamlit | Frontend UI |
| Groq API | LLM inference |
| Llama 3.3 70B | AI model |
| Python | Backend |
| HTML/CSS | Custom chat styling |

---

# 📦 Dependencies

```txt
streamlit>=1.35.0
openai>=1.30.0
python-dotenv>=1.0.0
```

---

# 📁 Export Support

Users can export conversations as:
- JSON
- TXT transcript

---

# 🚧 Future Improvements

- User authentication
- Database chat memory
- RAG with cybersecurity PDFs
- CVE lookup integration
- VirusTotal integration
- MITRE ATT&CK mapping
- File upload malware scanning
- Docker deployment
- Streaming responses

---

# 🤝 Contributing

Pull requests and suggestions are welcome.

If you'd like to improve:
- UI/UX
- cybersecurity datasets
- prompt security
- deployment setup

feel free to contribute.

---

# 📜 License

MIT License

---

# ⭐ Acknowledgements

- Groq
- Streamlit
- Open-source cybersecurity community

---

# 👨‍💻 Author

Annas Furquan pasha

GitHub:
https://github.com/Annas-Furquan-Pasha