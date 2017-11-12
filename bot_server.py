from flask import Flask
from flask import request
from app import handle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive():
    try:
        print(request.json)
        handle(request.json)
        return ""
    except Exception as e:
        print(e)
        return ""
