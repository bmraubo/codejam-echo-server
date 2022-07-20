import sys
import asyncio
import websockets

HOST = "localhost"
PORT = 4444

async def receive_message(socket):
    return socket.recv()

async def echo_message(socket):
    while True:
        message = await receive_message(socket)
        if message == "close":
            socket.close()
            sys.exit()
        await socket.send(message)

async def main():
    async with websockets.serve(echo_message, HOST, PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())