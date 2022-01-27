"""main file where we start flask server"""
# set FLASK_APP=main.py flask run
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run
import os
from itsdangerous import json
import requests
from flask import Flask, request, jsonify

# from other_module import fn_from_other_module
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery
images_collection = gallery.images

# adding .env.local to os.environ
load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError("create .env.local file & add UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = DEBUG
# DEBUG="" add in .env.local if you want debug=false


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


@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        # read images from db
        # returns cursor
        images = images_collection.find({})
        return jsonify([img for img in images])

    if request.method == "POST":
        # save image in db
        image = request.get_json()
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {"inserted_id": inserted_id}


if __name__ == "__main__":
    app.run("0.0.0.0", 5050)

# def hello():
#     return "Hello world"

# app.route('/')(hello)
