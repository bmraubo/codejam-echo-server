import websockets
from websockets.client import WebSocketClientProtocol
import typing

URI = "localhost:4444"

async def get_input() -> str:
    return await input("Enter message: ")

async def start_client() -> WebSocketClientProtocol:
    return await websockets.client.connect(URI)

async def send_message(connection: WebSocketClientProtocol, message: str):
    await connection.send(message)

async def receive_message(connection: WebSocketClientProtocol) -> str:
    await connection.recv()