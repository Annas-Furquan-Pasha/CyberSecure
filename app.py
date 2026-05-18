import streamlit as st
import time
import html

from prompt_guard import validate_prompt
from utils import (
    get_ai_response,
    get_timestamp,
    build_api_history,
    SAMPLE_QUESTIONS,
)

from ui import (
    apply_custom_css,
    render_sidebar,
    render_header,
    render_welcome_banner,
    render_chat_message,
)

# ---------------------------------------------------
# Page config
# ---------------------------------------------------

st.set_page_config(
    page_title="CyberSecure AI",
    page_icon="🔐",
    layout="wide",
)

# ---------------------------------------------------
# Apply UI
# ---------------------------------------------------

apply_custom_css()

# ---------------------------------------------------
# Session state
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_sample" not in st.session_state:
    st.session_state.pending_sample = None

if "total_queries" not in st.session_state:
    st.session_state.total_queries = 0

if "blocked_queries" not in st.session_state:
    st.session_state.blocked_queries = 0

if "last_request" not in st.session_state:
    st.session_state.last_request = 0

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

render_sidebar(
    st.session_state.messages,
    st.session_state.total_queries,
    st.session_state.blocked_queries,
    SAMPLE_QUESTIONS,
)

# Handle sample buttons
for q in SAMPLE_QUESTIONS[:8]:
    if st.session_state.get(f"sample_{hash(q)}"):
        st.session_state.pending_sample = q
        st.session_state[f"sample_{hash(q)}"] = False

# ---------------------------------------------------
# Header
# ---------------------------------------------------

render_header()

if not st.session_state.messages:
    render_welcome_banner()

# ---------------------------------------------------
# Render messages
# ---------------------------------------------------

for msg in st.session_state.messages:

    safe_content = html.escape(msg["content"])

    render_chat_message(
        role=msg["role"],
        content=safe_content,
        timestamp=msg.get("timestamp", "")
    )

# ---------------------------------------------------
# Input
# ---------------------------------------------------

prefill = st.session_state.pop("pending_sample", None) or ""

with st.form(key="chat_form", clear_on_submit=True):

    col1, col2 = st.columns([9, 1])

    with col1:
        user_input = st.text_input(
            "Message",
            value=prefill,
            placeholder="Ask cybersecurity questions...",
            label_visibility="collapsed",
        )

    with col2:
        send_clicked = st.form_submit_button(
            "Send ▶",
            use_container_width=True
        )

submit = send_clicked and user_input.strip()

# ---------------------------------------------------
# Main logic
# ---------------------------------------------------

if submit:

    # Rate limiting
    if time.time() - st.session_state.last_request < 2:
        st.warning("Please wait before sending another message.")
        st.stop()

    st.session_state.last_request = time.time()

    user_text = user_input.strip()
    
    timestamp = get_timestamp()

    is_valid, reason = validate_prompt(user_text)
    if reason == "greeting":

        greeting_reply = (
            "👋 Hello! I'm CyberSecure AI.\n\n"
            "Ask me anything about cybersecurity, SOC operations, "
            "ethical hacking, malware analysis, SIEM, or AI security."
        )

        st.session_state.messages.append({
            "role": "user",
            "content": user_text,
            "timestamp": timestamp,
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": greeting_reply,
            "timestamp": get_timestamp(),
        })

        st.rerun()

    st.session_state.total_queries += 1

    timestamp = get_timestamp()

    if not is_valid:

        st.session_state.blocked_queries += 1

        if reason == "injection":
            bot_reply = (
                "⛔ Prompt injection attempt detected and blocked.\n\n"
                "I can only assist with cybersecurity topics."
            )

        elif reason == "off_topic":
            bot_reply = (
                "🚫 I can only assist with cybersecurity topics."
            )

        else:
            bot_reply = "⚠️ Invalid request."

        st.session_state.messages.append({
            "role": "user",
            "content": user_text,
            "timestamp": timestamp,
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply,
            "timestamp": timestamp,
        })

        st.rerun()

    else:

        st.session_state.messages.append({
            "role": "user",
            "content": user_text,
            "timestamp": timestamp,
        })

        # Limit history
        MAX_HISTORY = 12
        st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]

        api_history = build_api_history(
            st.session_state.messages
        )

        with st.spinner("Analysing..."):

            try:
                reply = get_ai_response(api_history)

            except RuntimeError as e:
                reply = f"⚠️ Error: {e}"

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply,
            "timestamp": get_timestamp(),
        })

        st.rerun()