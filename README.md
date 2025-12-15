# Realtime AI Backend (WebSockets + Supabase) 🤖💬

## Overview
Realtime AI Backend is an async Python system using FastAPI and WebSockets for real-time AI conversations, storing session data in Supabase and generating post-session summaries, showcasing low-latency interaction, state management, and automation in a single backend. 

**Key functionalities:**  
- Users send messages via WebSocket  
- AI responses are streamed in real-time  
- All messages and events are saved in Supabase  
- After the session ends, an AI-generated summary is stored automatically  

---

## Features ✨
- Real-time messaging with token-by-token AI streaming   
- Supports complex LLM interactions (function/tool calls, multi-step workflows)  
- Session and event logging in Supabase  
- Post-session summary generation   
- Simple, interactive dark-mode frontend   

---

## Tech Stack 🛠️
- **Backend:** Python, FastAPI   
- **Database:** Supabase (PostgreSQL)   
- **WebSockets:** FastAPI WebSocket API   
- **LLM:** OpenAI API or similar  
- **Frontend:** HTML + JavaScript  

---
## Setup & Installation 🚀

1. **Clone the repository**
```bash
git clone <YOUR_REPO_URL>
cd realtime-ai-backend
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Add environment variables (.env)

ini
Copy code
SUPABASE_URL=<YOUR_SUPABASE_URL>
SUPABASE_KEY=<YOUR_SUPABASE_KEY>
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
Run the backend server

bash
Copy code
uvicorn backend.main:app --reload
Open frontend

Open frontend/index.html in a browser 🌐

Start chatting via WebSocket 💬

Database Schema (Supabase) 🗄️
Sessions Table
sql
Copy code
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    start_time TIMESTAMP DEFAULT now(),
    end_time TIMESTAMP,
    summary TEXT
);
Event Log Table
sql
Copy code
CREATE TABLE session_events (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(session_id),
    event_type TEXT,       -- user_message / ai_response / tool_call
    content TEXT,
    created_at TIMESTAMP DEFAULT now()
);
WebSocket Workflow 🔄
Client connects:
ws://localhost:8000/ws/session/{session_id}

User sends messages 📨 → AI streams response ⚡ → all events saved in Supabase 💾

On disconnect 🔌 → backend generates session summary 📝 → updates session record

Screenshots 📸
Chat Interface 💬

AI Streaming ⚡

Session Summary 📝
