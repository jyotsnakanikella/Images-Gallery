# set FLASK_APP=main.py flask run
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run
import requests
from flask import Flask, request
from other_module import fn_from_other_module

UNSPLASH_URL = 'https://api.unsplash.com/photos/random'
UNSPLASH_KEY = 'A2bFuGDleVlHlUkasCuEGxC-yqhtR3b6Hytp62ttAoQ'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"
  
@app.route("/new-image")  
def new_image():
    word = request.args.get("query")
    headers = {
      "Accept-Version":"v1",
      "Authorization": f"Client-ID {UNSPLASH_KEY}"
    }
    payload = {
      "query":f"{word}"
    }
    response = requests.get(url=UNSPLASH_URL,headers=headers,params=payload)
    data = response.json() 
    return data
  
if __name__ == '__main__':
  app.run("0.0.0.0",5050) 

# def hello():
#     return "Hello world"
  
# app.route('/')(hello)  