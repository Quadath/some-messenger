from aioflask import *
from flask import send_from_directory
import os
import json
from flask_cors import CORS, cross_origin

import time
from tinydb import TinyDB, Query

app = Flask(__name__)
cors = CORS(app, resources={r"/post": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
db = TinyDB('database/db.json')

@app.route('/post', methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def post():
    content = request.json
    print(content['username'])
    return jsonify({'answer': True})
    
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

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

app.run(host="0.0.0.0", port=5000, static_url_path='')
    