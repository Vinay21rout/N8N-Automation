# 🤖 N8N Automation — AI Workflows Collection

A growing collection of **n8n** automation workflows with AI capabilities, each paired with a Streamlit UI, exported workflow JSON, screenshots, and dedicated documentation.

---

## 📸 Workflow Preview

![n8n Workflow](./screenshots/Screenshot%202026-03-23%20094346.png)

---

## 📁 Repository Structure

```
N8N-Automation/
├── chatbot_with_tools/
│   ├── app.py                  # Streamlit chat UI
│   ├── My workflow (1).json    # Exported n8n workflow
│   ├── requirements.txt
│   └── README.md
├── screenshots/
│   └── Screenshot 2026-03-23 094346.png
└── README.md                   # This file
```

> Each workflow folder is fully self-contained — UI, workflow JSON, screenshots, and docs.

---

## 🗂️ Workflows

| # | Workflow | Description | Stack | Status |
|---|---|---|---|---|
| 1 | [chatbot_with_tools](./chatbot_with_tools/) | AI chatbot with memory, web search & event tools | n8n + Groq + Streamlit | ✅ Live |
| 2 | More coming... | — | — | 🔜 Planned |

---

## ⚙️ Common Architecture

Every workflow in this repo follows the same base pattern:

```
Streamlit UI  →  POST /webhook  →  n8n AI Agent  →  Tools  →  Response
```

| Component | Role |
|---|---|
| Streamlit UI | Chat interface for user input/output |
| n8n Webhook | Entry point that receives user queries |
| Groq Chat Model | Fast LLM for low-latency AI responses |
| Memory Node | Maintains conversation context across turns |
| Tools | Pluggable — search, events, APIs, etc. |
| Respond to Webhook | Sends AI response back to Streamlit |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Vinay21rout/N8N-Automation.git
cd N8N-Automation
```

### 2. Start n8n locally

```bash
npx n8n
```

### 3. Import a workflow

- Open n8n at `http://localhost:5678`
- Go to **Workflows → Import**
- Select the `workflow.json` from any workflow folder

### 4. Run the UI

```bash
cd chatbot_with_tools
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔗 Webhook Payload

All workflows use a consistent payload format:

```json
{ "query": "your message here" }
```

Response:

```json
{ "output": "AI response here" }
```

---

## 🔮 Upcoming Workflows

- 🗓️ Google Calendar AI Assistant
- 📧 Gmail Automation Agent
- 📊 Google Sheets Data Analyst
- 🔔 Slack Notification Bot
- 🧠 RAG — PDF Knowledge Base Chatbot
- 🤖 Multi-Agent System

---

## 📡 Integration Roadmap

| Platform | Status |
|---|---|
| Streamlit | ✅ Implemented |
| Telegram Bot | 🔜 Planned |
| Gmail API | 🔜 Planned |
| Google Calendar | 🔜 Planned |
| Notion / Slack | 🔜 Planned |
| Custom React Frontend | 🔜 Planned |
