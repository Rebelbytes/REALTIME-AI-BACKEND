
# Realtime AI Backend (WebSockets + Supabase) 🤖💬

## Overview
Realtime AI Backend is an asynchronous Python system using FastAPI and WebSockets for real-time AI conversations. It stores session data in Supabase and generates post-session summaries, showcasing low-latency interaction, state management, and automation in a single backend.

---

## Features ✨
- Real-time messaging with token-by-token AI streaming  
- Supports complex LLM interactions (function/tool calls, multi-step workflows)  
- Session and event logging in Supabase  
- Post-session summary generation  
- Simple, interactive frontend  

---

## Tech Stack 🛠️
- **Backend:** Python, FastAPI  
- **Database:** Supabase (PostgreSQL)  
- **WebSockets:** FastAPI WebSocket API  
- **LLM:** OpenAI API or similar  
- **Frontend:** HTML + JavaScript  

---

## Architecture 🏗️
The system consists of a frontend client, a FastAPI WebSocket server, an LLM layer, and a Supabase database. Users send messages via WebSocket, the server streams AI responses back in real-time, logs all events asynchronously in Supabase, and triggers a post-session job to generate a session summary.

![Realtime AI Backend Architecture](realtime_ai_backend/assets/Architecture.jpg)

---

## Setup ⚙️

### 1. Create a virtual environment
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add environment variables (.env)

```
SUPABASE_URL=<YOUR_SUPABASE_URL>
SUPABASE_KEY=<YOUR_SUPABASE_KEY>
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

### 4. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 5. Open frontend

* Open `frontend/index.html` in a browser 🌐
* Start chatting via WebSocket 💬

---

## Database Schema (Supabase) 🗄️

### Sessions Table

```sql
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    start_time TIMESTAMP DEFAULT now(),
    end_time TIMESTAMP,
    summary TEXT
);
```

### Event Log Table

```sql
CREATE TABLE session_events (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(session_id),
    event_type TEXT,       -- user_message / ai_response / tool_call
    content TEXT,
    created_at TIMESTAMP DEFAULT now()
);
```

---

## WebSocket Workflow 🔄

1. Client connects:

```
ws://localhost:8000/ws/session/{session_id}
```

2. User sends messages 📨 → AI streams response ⚡ → all events saved in Supabase 💾

3. On disconnect 🔌 → backend generates session summary 📝 → updates session record

---

## Screenshots 📸

* Chat Interface 💬
* AI Streaming ⚡
* Session Summary 📝

```

---

### ✅ **Next Steps to Push to GitHub**
1. Save this content in your `README.md`.
2. Make sure the architecture image is in:  
```

realtime_ai_backend/assets/Architecture.jpg

````
3. Run the following commands in PowerShell:

```powershell
git add README.md realtime_ai_backend/assets/Architecture.jpg
git commit -m "Polished README with architecture diagram, setup, workflow"
git push origin main
````


