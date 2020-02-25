import asyncio
import websockets

global config

async def echo(websocket, path):
    global config
    async for message in websocket:
        await websocket.send(message)
        config = message
        if config != '':
            asyncio.get_event_loop().stop()

def importConfig(address, port):
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, address, port))
    asyncio.get_event_loop().run_forever()










#!/usr/bin/env python

# import asyncio
# import websockets
#
# async def hello():
#     uri = "ws://192.168.43.201:255"
#     async with websockets.connect(uri) as websocket:
#         #await websocket.send("Hello world!")
#         t=await websocket.recv()
#     print(t)
# asyncio.get_event_loop().run_until_complete(hello())


