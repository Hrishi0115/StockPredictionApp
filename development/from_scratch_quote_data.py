# real-time websocket

import os
from dotenv import load_dotenv

# load environment variables from .env file

load_dotenv()

# get API key from environment variables

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

import asyncio
import websockets
import json

async def subscribe_to_alpaca(api_key, api_secret):
    url = "wss://stream.data.alpaca.markets/v2/iex"

    async with websockets.connect(url) as websocket:
        # Authenticate
        auth_message = {
            "action": "auth",
            "key": api_key,
            "secret": api_secret
        }
        await websocket.send(json.dumps(auth_message))
        response = await websocket.recv()
        print(f"Auth response: {response}")

        # Subscribe to data
        subscribe_message = {
            "action": "subscribe",
            "trades": [],
            "quotes": ['AAPL'],
            "bars": []
        }
        await websocket.send(json.dumps(subscribe_message))
        response = await websocket.recv()
        print(f"Subscribe response: {response}")

        # Listen to incoming messages
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")


# Run the subscription
asyncio.get_event_loop().run_until_complete(subscribe_to_alpaca(api_key, api_secret))

# Received message: [{"T":"q","S":"AAPL","bx":"V","bp":192.9,"bs":1,"ax":"V","ap":194,"as":14,"c":["R"],"z":"C","t":"2024-06-03T13:33:33.002960334Z"}]

# [
#   {
#     "T": "q",                   // Type of message: 'q' for quote
#     "S": "AAPL",                // Symbol: AAPL (Apple Inc.)
#     "bx": "V",                  // Bid exchange: V (Exchange code)
#     "bp": 192.9,                // Bid price: 192.9 USD
#     "bs": 1,                    // Bid size: 1 (number of shares)
#     "ax": "V",                  // Ask exchange: V (Exchange code)
#     "ap": 194,                  // Ask price: 194 USD
#     "as": 14,                   // Ask size: 14 (number of shares)
#     "c": ["R"],                 // Condition codes: ["R"] (list of codes)
#     "z": "C",                   // Tape: C (Consolidated tape)
#     "t": "2024-06-03T13:33:33.002960334Z" // Timestamp: 2024-06-03T13:33:33.002960334Z (ISO 8601 format)
#   }
# ]

# quote: represents the most recent bid and ask price
# gives traders the current market price to buy (ask) or sell (bid) a security
# bid: highest price that a buyer is willing to pay for a security - represents the demand side of the market
# ask (/offer): lowest price at which a seller is willing to sell a security - represents the supply side of the market
# bid size: number of shares a buyer is willing to purchase at the bid price - vice versa for sell size
# 
