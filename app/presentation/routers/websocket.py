from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect
from app.di import containers

websock = APIRouter()

@websock.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    '''Websocket endpoint'''
    containers.websocket.clients.add(websocket)
    try:
        await websocket.accept()

        while True:
            message = await websocket.receive_text()
            print("Received message from client:", message)
    except WebSocketDisconnect:
        containers.websocket.clients.remove(websocket)
        print("Client disconnected")