"""
utils.py
--------
Utility functions using Groq API (OpenAI-compatible).
"""

import os
import json
import datetime
from typing import List, Dict

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from openai import OpenAI
from prompt_guard import build_system_prompt

# ---------------------------------------------------------------------------
# Configure Groq client
# ---------------------------------------------------------------------------

def get_client():
    """Initialize and return Groq client."""

    api_key = os.environ.get("GROQ_API_KEY", "")

    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GROQ_API_KEY", "")
        except Exception:
            pass

    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY is not set. "
            "Add it to your .env file or Streamlit secrets."
        )

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )


# ---------------------------------------------------------------------------
# LLM interaction
# ---------------------------------------------------------------------------

def get_ai_response(conversation_history: List[Dict[str, str]]) -> str:
    """
    Send conversation history to Groq and return the reply.
    """

    try:
        client = get_client()

        messages = [
            {
                "role": "system",
                "content": build_system_prompt()
            }
        ]

        # Add chat history
        for msg in conversation_history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.3,
            max_tokens=700,
        )

        return response.choices[0].message.content

    except EnvironmentError as e:
        raise RuntimeError(str(e)) from e

    except Exception as e:
        error_msg = str(e)

        if "rate_limit" in error_msg.lower():
            raise RuntimeError(
                "⏳ Rate limit reached. Please wait and try again."
            ) from e

        elif "api key" in error_msg.lower():
            raise RuntimeError(
                "❌ Invalid GROQ API key."
            ) from e

        else:
            raise RuntimeError(
                f"⚠️ API error: {error_msg}"
            ) from e


# ---------------------------------------------------------------------------
# Timestamp helpers
# ---------------------------------------------------------------------------

def get_timestamp() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_date_header() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Chat history helpers
# ---------------------------------------------------------------------------

def build_api_history(messages: List[Dict]) -> List[Dict[str, str]]:
    """Return only role + content fields for API use."""
    return [{"role": m["role"], "content": m["content"]} for m in messages]


def export_chat_history(messages: List[Dict]) -> str:
    export_data = {
        "exported_at": datetime.datetime.now().isoformat(),
        "application": "CyberSecure AI Assistant",
        "message_count": len(messages),
        "messages": messages,
    }

    return json.dumps(export_data, indent=2, ensure_ascii=False)


def export_chat_as_text(messages: List[Dict]) -> str:
    lines = [
        "=" * 60,
        "  CyberSecure AI Assistant — Chat Transcript",
        f"  Exported: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 60,
        "",
    ]

    for m in messages:
        role_label = "You" if m["role"] == "user" else "CyberSecure AI"
        ts = m.get("timestamp", "")

        lines.append(f"[{ts}] {role_label}:")
        lines.append(m["content"])
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sample questions
# ---------------------------------------------------------------------------

SAMPLE_QUESTIONS = [
    "🔍 What is a SIEM and how does it work?",
    "🛡️ Explain the MITRE ATT&CK framework",
    "🐛 How does ransomware work and how do I detect it?",
    "🔐 What is penetration testing methodology?",
    "📊 How to build a Splunk dashboard for threat detection?",
    "🤖 How is AI used in cybersecurity threat detection?",
    "🌐 What are the OWASP Top 10 vulnerabilities?",
    "🧩 How do I start a career in cybersecurity / SOC?",
    "💡 What is the difference between IDS and IPS?",
    "🔑 Explain Zero Trust architecture",
    "📡 How to analyse a suspicious network packet capture?",
    "⚠️ What is a supply chain attack? Give recent examples.",
]