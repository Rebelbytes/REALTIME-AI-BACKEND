from fastapi import WebSocket
from db import supabase
from llm import fake_llm_stream, fetch_sales_data
from post_session import generate_summary
import asyncio
from datetime import datetime

def now_iso():
    return datetime.utcnow().isoformat()

async def websocket_session(websocket: WebSocket, session_id: str):
    await websocket.accept()

    # Create session in Supabase
    supabase.table("sessions").insert({
        "session_id": session_id,
        "start_time": now_iso()
    }).execute()

    messages = []

    try:
        while True:
            data = await websocket.receive_json()
            user_msg = data["message"]
            user_id = data.get("user_id", "unknown")

            # Save user message
            supabase.table("session_events").insert({
                "session_id": session_id,
                "event_type": "user_message",
                "content": user_msg,
                "created_at": now_iso()
            }).execute()

            messages.append({"role": "user", "content": user_msg})

            # Tool call if user asks about data
            if "data" in user_msg.lower():
                tool_result = fetch_sales_data()
                messages.append({"role": "tool", "content": str(tool_result)})

            # Stream AI response
            ai_response = ""
            async for token in fake_llm_stream(messages):
                ai_response += token
                await websocket.send_text(token)

            # Save AI response
            supabase.table("session_events").insert({
                "session_id": session_id,
                "event_type": "ai_message",
                "content": ai_response,
                "created_at": now_iso()
            }).execute()

    except Exception:
        # Post-session summary on disconnect
        await generate_summary(session_id)
        await websocket.close()
