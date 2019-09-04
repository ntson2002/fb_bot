from flask import Flask, request, jsonify, Response
import json
from routes import *

app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)