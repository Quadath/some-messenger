from aioflask import Flask, request
import os
import json

from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import EditMessageRequest
import time

APP_ID = '19110082'
API_HASH = 'a7dd11527616ba229c1dee2405588006'

app = Flask(__name__)

async def sendMessage(data, nickname='Quadath'):
    async with TelegramClient('tg-account', APP_ID, API_HASH) as client:
       await client.send_message(nickname, data)
    return 'all-OK'

@app.route('/post', methods=['POST'])
async def post():
    information = request.data.decode('utf-8')
    print(information)
    await sendMessage(information)
    return '200'
    
@app.route("/", methods=['GET'])
async def index():
    html = open('index.html')
    return html.read()
app.run(host="0.0.0.0", port=5000)
    