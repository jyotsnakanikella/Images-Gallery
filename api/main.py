# set FLASK_APP=main.py flask run
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run
from flask import Flask
from other_module import fn_from_other_module

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"
  
if __name__ == '__main__':
  app.run("0.0.0.0",5050) 

# def hello():
#     return "Hello world"
  
# app.route('/')(hello)  