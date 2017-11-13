from flask import Flask
from flask import request
from app import handle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive():
    try:
        handle(request.json)
        return True
    except Exception as e:
        print(e)
        return ""
