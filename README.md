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

## Architecture 🏗️
The system consists of a frontend client, a FastAPI WebSocket server, an LLM layer, and a Supabase database. Users send messages via WebSocket, the server streams AI responses back in real-time, logs all events asynchronously in Supabase, and triggers a post-session job to generate a session summary.
![Realtime AI Backend Architecture](assets/architecture.jpg)

---

## Setup & Installation 🚀

