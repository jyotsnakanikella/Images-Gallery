"""main file where we start flask server"""
# set FLASK_APP=main.py flask run
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run
import os
import requests
from flask import Flask, request

# from other_module import fn_from_other_module
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import insert_test_document

# adding .env.local to os.environ
load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and insert UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = DEBUG
# DEBUG="" add in .env.local if you want debug=false
insert_test_document()


@app.route("/")
def hello():
    """sample fn"""
    return "Hello world"


@app.route("/new-image")
def new_image():
    """create new image url"""
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {UNSPLASH_KEY}",
    }
    payload = {"query": f"{word}"}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=payload)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run("0.0.0.0", 5050)

# def hello():
#     return "Hello world"

# app.route('/')(hello)
