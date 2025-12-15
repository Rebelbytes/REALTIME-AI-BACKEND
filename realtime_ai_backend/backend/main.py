from fastapi import FastAPI, WebSocket
from websocket import websocket_session

app = FastAPI()

@app.websocket("/ws/session/{session_id}")
async def ws_endpoint(websocket: WebSocket, session_id: str):
    await websocket_session(websocket, session_id)

# Optional: Root route to avoid 404
@app.get("/")
def read_root():
    return {"message": "Realtime AI Backend is running!"}