import sys
import asyncio
import uvicorn
from starlette.websockets import WebSocket
from starlette.routing import WebSocketRoute
from starlette.applications import Starlette

HOST = "localhost"
PORT = 4444

async def app(scope, receive, send):
    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    message: str = await websocket.receive_text()
    await websocket.send_text(message)
    if message == "close":
        await websocket.close()
        sys.exit()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=4444, debug=True)