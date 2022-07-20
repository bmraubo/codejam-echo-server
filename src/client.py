import websockets
from websockets.client import WebSocketClientProtocol
import typing
import asyncio

URI = "localhost:4444"

async def get_input() -> str:
    return await input("Enter message: ")

async def start_client() -> WebSocketClientProtocol:
    return await websockets.client.connect(URI)

async def send_message(connection: WebSocketClientProtocol, message: str):
    await connection.send(message)

async def receive_message(connection: WebSocketClientProtocol) -> str:
    await connection.recv()

async def main():
    while True:
        connection = await start_client()
        message = await get_input()
        await send_message(connection, message)
        received = await receive_message(connection)
        print(received)

if __name__ == "__main__":
    asyncio.run(main())