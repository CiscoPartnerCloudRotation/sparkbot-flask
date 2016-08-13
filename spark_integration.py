# -*- coding: utf-8 -*-

import requests
import json
import ast
import time
from flask import Flask
from flask import request
import os

# Run a flask endpoint
app = Flask(__name__)

# This will hold a list of all messages that contain a keyword, that we've already seen
# so that we don't parse the same message twice
parsed_kw_messages = []
keywords = ["lunch", "food"]

AUTH_KEY = os.environ['AUTH_KEY']
ROOM_ID = os.environ['ROOM_ID']

@app.route('/')
def confirm_service():
    return "Service OK"

@app.route('/post_result', methods=["POST"])
def post_result():
    headers = {}        # empty dictionary
    headers["Authorization"] = AUTH_KEY
    headers["Content-Type"] = "application/json; charset=utf-8"

    data = {"roomId" : ROOM_ID}

    data['text'] = request.args.get('message')
    r = requests.post("https://api.ciscospark.com/v1/messages", headers=headers, json=data)
    return "Ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
