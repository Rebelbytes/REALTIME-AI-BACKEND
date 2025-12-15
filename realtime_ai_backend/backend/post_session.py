from db import supabase
from datetime import datetime

def now_iso():
    return datetime.utcnow().isoformat()

async def generate_summary(session_id):
    events_response = supabase.table("session_events") \
        .select("event_type, content") \
        .eq("session_id", session_id) \
        .execute()

    events = events_response.data if events_response.data else []

    summary = "Session Summary:\n"
    for e in events:
        summary += f"{e['event_type']}: {e['content']}\n"

    supabase.table("sessions").update({
        "summary": summary,
        "end_time": now_iso()
    }).eq("session_id", session_id).execute()
