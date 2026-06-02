import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/system")
def system():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent
    })
