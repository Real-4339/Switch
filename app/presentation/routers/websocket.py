import json

from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect
from app.di import containers


connected_clients = set()
websock = APIRouter()

@containers.websocket.set_mac_update
async def broadcast_mac_table(mac_table: dict):
    # Set data
    data = {"type": "updateMacTable", "macTable": list(mac_table)}
    json_data = json.dumps(data)

    for client in connected_clients:
        await client.send_text(json_data)

@websock.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    '''Websocket endpoint'''
    connected_clients.add(websocket)
    try:
        await websocket.accept()

        while True:
            message = await websocket.receive_text()
            print("Received message from client:", message)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected")



