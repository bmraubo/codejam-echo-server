import websockets
from websockets.client import WebSocketClientProtocol
import typing
import asyncio
import sys

URI = "ws://localhost:4444"

def get_input() -> str:
    return input("Enter message: ")

async def start_client() -> WebSocketClientProtocol:
    return await websockets.client.connect(URI)

async def send_message(connection: WebSocketClientProtocol, message: str):
    await connection.send(message)

async def receive_message(connection: WebSocketClientProtocol) -> str:
    return await connection.recv()

async def main():
    while True:
        connection = await start_client()
        message = get_input()
        await send_message(connection, message)
        received = await receive_message(connection)
        print(received)
        if message == "close":
            sys.exit()

if __name__ == "__main__":
    asyncio.run(main())