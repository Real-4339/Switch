from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect

connected_clients = set()

websock = APIRouter()

@websock.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    connected_clients.add(websocket)
    try:
        await websocket.accept()

        while True:
            message = await websocket.receive_text()
            print("Received message from client:", message)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected")
    