import streamlit as st
import requests

# ── Config ─────────────────────────────────────────────────
WEBHOOK_URL = "http://localhost:5678/webhook-test/3590b417-0429-423d-b1c7-7a9fbaba6dca"

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Assistant")
st.caption("Powered by n8n + Groq")

# ── Session state for chat history ─────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Display chat history ────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ──────────────────────────────────────────────
if prompt := st.chat_input("Ask me anything..."):

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to n8n webhook
    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                WEBHOOK_URL,
                json={"query": prompt},
            )

            # ── Check if response is empty ─────────────────
            if not res.text or res.text.strip() == "":
                answer = "⚠️ n8n returned empty response. Check workflow!"
            else:
                try:
                    data   = res.json()
                    answer = (data.get("output")   or
                              data.get("response") or
                              data.get("answer")   or
                              data.get("text")     or
                              str(data))
                except Exception:
                    answer = res.json()[0]["output"]

        except requests.exceptions.ConnectionError:
            answer = "❌ n8n not running! Start: npx n8n"
        except requests.exceptions.Timeout:
            answer = "⏳ Timeout! n8n took too long."
        except Exception as e:
            answer = f"❌ Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })