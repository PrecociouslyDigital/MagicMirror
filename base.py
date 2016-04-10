#!/usr/bin/env python3.5

import asyncio
import random
import websockets
import datetime
import json

async def createFriends(websocket, path):
    while True:
        sending = {
        	"command" : "create",
        	"data":{
	        	"html": datetime.datetime.utcnow().isoformat() + 'Z',
	        	"position":{
	        		"x": str(100 * random.random()) ,
	        		"y": str(100 * random.random()) 
	        	}
	        }
        }
        await websocket.send(json.dumps(sending))
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(createFriends, '127.0.0.1', 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()