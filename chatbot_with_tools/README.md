# 🤖 AI Workflow Automation — n8n + Streamlit

An AI-powered chatbot interface built with **Streamlit**, connected to an **n8n** workflow that uses **Groq** as the LLM backend with tool calling, memory, and webhook-based communication.

---

## 📸 Workflow

![n8n Workflow](../screenshots/chatbot_with_tools_workflow_image.png)

---

## 📁 Project Structure

```
chatbot_with_tools/
├── app.py              # Streamlit chat UI connected to n8n webhook
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ Architecture

```
Streamlit UI  →  POST /webhook  →  n8n AI Agent  →  Tools  →  Response
```

| Component | Role |
|---|---|
| Streamlit UI | Chat interface for user input/output |
| n8n Webhook | Entry point that receives queries |
| Groq Chat Model | Fast LLM for low-latency AI responses |
| Memory Node | Maintains conversation context across turns |
| Event Tools | Create and fetch events |
| SerpAPI | Real-time web search |
| Respond to Webhook | Sends AI response back to Streamlit |

---

## ✨ Features

- ⚡ Fast AI responses via Groq
- 🧠 Context-aware conversations with memory
- 🛠️ Tool calling — event APIs + web search
- 🔗 Webhook-based integration with n8n
- 💬 Clean Streamlit chat interface

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start n8n locally

```bash
npx n8n
```

### 3. Configure webhook URL

In `app.py`, update:

```python
WEBHOOK_URL = "http://localhost:5678/webhook-test/<your-webhook-id>"
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔗 Webhook Payload

Streamlit sends the following JSON to n8n on every message:

```json
{ "query": "your message here" }
```

n8n responds with:

```json
{ "output": "AI response here" }
```

---

## 🚀 Use Cases

- Personal AI Assistant
- Task / Event Manager
- Study Assistant
- Chatbot with real-time web search
- Productivity automation system

---

## 🔮 Future Enhancements

- 🔗 Telegram / WhatsApp integration
- 🧠 RAG — PDF + knowledge base support
- 🤖 Multi-agent system
- 🎙️ Voice input/output
- 🗄️ Database integration (Firebase / MongoDB)
- 🔐 Authentication & user management

---

## 📡 Integration Ideas

| Platform | Status |
|---|---|
| Streamlit | ✅ Implemented |
| Telegram Bot | 🔜 Planned |
| Gmail API | 🔜 Planned |
| Google Calendar | 🔜 Planned |
| Notion / Slack | 🔜 Planned |
| Custom React Frontend | 🔜 Planned |

---

## 🛠️ Requirements

```
streamlit
requests
```
