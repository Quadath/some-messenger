from aioflask import Flask, request, send_file, jsonify
import os
import json

import time
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('database/db.json')

@app.route('/post', methods=['POST'])
async def post():
    information = request.data.decode('utf-8')
    print(db.all())
    db.insert({"text": information, "id": len(db.all())})
    return '200'
    
@app.route("/", methods=['GET'])
async def index():
    html = open('index.html')
    return html.read()

@app.route("/script",  methods=['GET'])
async def script():
	return send_file("index.js")

@app.route("/data", methods=['GET'])
async def data():
    db = open('database/db.json')
    return jsonify(db.read())
app.run(host="0.0.0.0", port=5000)
    