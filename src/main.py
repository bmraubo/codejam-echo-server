import sys
import asyncio
from fastapi import FastAPI, WebSocket
import uvicorn


HOST = "localhost"
PORT = 4444

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)
        if message == "close":
            websocket.close()
            sys.exit()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=4444, debug=True)