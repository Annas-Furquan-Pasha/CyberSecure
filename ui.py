import streamlit as st

from utils import (
    export_chat_history,
    export_chat_as_text,
    get_date_header,
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

def apply_custom_css():

    st.markdown(
        """
        <style>

        /* -------------------------------------------------- */
        /* Global */
        /* -------------------------------------------------- */

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #020b18 !important;
            color: #d6eaff !important;
            font-family: 'Segoe UI', sans-serif;
        }

        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* -------------------------------------------------- */
        /* Sidebar */
        /* -------------------------------------------------- */

        [data-testid="stSidebar"] {
            background: #06121f !important;
            border-right: 1px solid rgba(0,212,255,0.15);
        }

        [data-testid="stSidebar"] * {
            color: #d6eaff !important;
        }

        /* -------------------------------------------------- */
        /* Header */
        /* -------------------------------------------------- */

        .header {
            text-align: center;
            color: #00d4ff;
            font-size: 2.3rem;
            font-weight: 700;
            margin-top: 10px;
            letter-spacing: 2px;
        }

        .subheader {
            text-align: center;
            color: #7eaac7;
            margin-bottom: 25px;
            font-size: 0.95rem;
        }

        /* -------------------------------------------------- */
        /* Chat Bubbles */
        /* -------------------------------------------------- */

        .chat-user {
            background: linear-gradient(135deg, #004060, #005c8a);
            padding: 16px;
            border-radius: 16px;
            margin-bottom: 14px;
            border: 1px solid rgba(0,212,255,0.2);
            box-shadow: 0 0 12px rgba(0,212,255,0.08);
        }

        .chat-bot {
            background: linear-gradient(135deg, #012218, #013326);
            padding: 16px;
            border-radius: 16px;
            margin-bottom: 14px;
            border: 1px solid rgba(0,255,136,0.15);
            box-shadow: 0 0 12px rgba(0,255,136,0.06);
        }

        /* -------------------------------------------------- */
        /* Input */
        /* -------------------------------------------------- */

        .stTextInput input {
            background-color: #071625 !important;
            color: #d6eaff !important;
            border: 1px solid rgba(0,212,255,0.25) !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        .stTextInput input:focus {
            border: 1px solid #00d4ff !important;
            box-shadow: 0 0 10px rgba(0,212,255,0.2);
        }

        /* -------------------------------------------------- */
        /* Buttons */
        /* -------------------------------------------------- */

        .stButton button {
            background: linear-gradient(135deg, #004060, #005c8a) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 10px !important;
            font-weight: 600 !important;
            transition: 0.2s ease !important;
        }

        .stButton button:hover {
            transform: translateY(-1px);
            box-shadow: 0 0 12px rgba(0,212,255,0.25);
        }

        /* -------------------------------------------------- */
        /* Download Buttons */
        /* -------------------------------------------------- */

        .stDownloadButton button {
            background: linear-gradient(135deg, #013326, #01593f) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 10px !important;
        }

        /* -------------------------------------------------- */
        /* Metrics */
        /* -------------------------------------------------- */

        [data-testid="metric-container"] {
            background: #071625;
            border: 1px solid rgba(0,212,255,0.12);
            padding: 10px;
            border-radius: 14px;
        }

        /* -------------------------------------------------- */
        /* Spinner */
        /* -------------------------------------------------- */

        .stSpinner {
            color: #00d4ff !important;
        }

        /* -------------------------------------------------- */
        /* Scrollbar */
        /* -------------------------------------------------- */

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(0,212,255,0.25);
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------
# Header
# ---------------------------------------------------

def render_header():

    st.markdown(
        "<div class='header'>⚡ CYBERSECURE AI ASSISTANT ⚡</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='subheader'>Threat Intelligence • SOC • Ethical Hacking</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------
# Welcome banner
# ---------------------------------------------------

def render_welcome_banner():

    st.info(
        "👋 Welcome to CyberSecure AI! "
        "Ask anything about cybersecurity, SIEM, SOC, malware, pentesting, or AI security."
    )

# ---------------------------------------------------
# Chat messages
# ---------------------------------------------------

def render_chat_message(role, content, timestamp):

    if role == "user":

        st.markdown(
            f"""
<div style="
display:flex;
justify-content:flex-end;
margin-bottom:14px;
">

<div style="
background: linear-gradient(135deg,#005c8a,#0077b6);
color:white;
padding:14px;
border-radius:18px 18px 4px 18px;
max-width:75%;
box-shadow:0 0 10px rgba(0,212,255,0.12);
border:1px solid rgba(0,212,255,0.2);
">

<div style="
font-size:15px;
line-height:1.6;
">
{content}
</div>

<div style="
text-align:right;
font-size:11px;
opacity:0.7;
margin-top:6px;
">
{timestamp}
</div>

</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            f"""
<div style="
display:flex;
justify-content:flex-start;
margin-bottom:14px;
">

<div style="
background: linear-gradient(135deg,#012218,#013d2c);
color:#d8ffe8;
padding:14px;
border-radius:18px 18px 18px 4px;
max-width:75%;
box-shadow:0 0 10px rgba(0,255,136,0.08);
border:1px solid rgba(0,255,136,0.15);
">

<div style="
font-size:15px;
line-height:1.6;
">
{content}
</div>

<div style="
text-align:right;
font-size:11px;
opacity:0.7;
margin-top:6px;
">
{timestamp}
</div>

</div>
</div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

def render_sidebar(
    messages,
    total_queries,
    blocked_queries,
    sample_questions
):

    with st.sidebar:

        st.title("🔐 CyberSecure AI")

        st.caption("Cybersecurity Intelligence Platform")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Queries", total_queries)

        with col2:
            st.metric("Blocked", blocked_queries)

        st.divider()

        st.subheader("Sample Questions")

        for q in sample_questions[:8]:

            st.button(
                q,
                key=f"sample_{hash(q)}",
                use_container_width=True,
            )

        st.divider()

        if st.button(
            "🗑️ Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []
            st.session_state.total_queries = 0
            st.session_state.blocked_queries = 0

            st.rerun()

        if messages:

            json_data = export_chat_history(messages)

            st.download_button(
                label="⬇️ Download JSON",
                data=json_data,
                file_name=f"cybersecure_chat_{get_date_header()}.json",
                mime="application/json",
                use_container_width=True,
            )

            txt_data = export_chat_as_text(messages)

            st.download_button(
                label="⬇️ Download TXT",
                data=txt_data,
                file_name=f"cybersecure_chat_{get_date_header()}.txt",
                mime="text/plain",
                use_container_width=True,
            )

        st.divider()

        st.caption("Powered by Groq + Llama 3.3")