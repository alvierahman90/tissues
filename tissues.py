#!/usr/bin/env python3

import sys
import os
import json
from flask import Flask
from flask import render_template
from flask import request
import telepot

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

with open('config.json') as file:
    config = json.loads(file.read())
bot = telepot.Bot(config['token'])
chat_id = config['chat_id']


@app.route("/")
@app.route("/request_tissue", methods=["GET", "POST"])
def submit_tissue():
    if request.method == "POST":
        product = request.values.get("product")
        issue = request.values.get("issue")
        name = request.values.get("name")
        other = request.values.get("other")
        love = "Yes" if request.values.get("love") == "on" else "No"

        message = "New issue\n"
        message += f"Product: {product}\n"
        message += f"User: {name}\n"
        message += f"Love: {love}\n"
        message += f"Issue: \n"
        message += issue
        bot.sendMessage(chat_id, message)
        return render_template("std.html", message="A tissue has been requested and it may be considered")
    else:
        return render_template('request_tissue.html')

    
if __name__ == "__main__":
    app.debug = True
    app.run()
