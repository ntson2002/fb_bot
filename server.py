from flask import Flask, request, jsonify, Response
import json
from routes import *

app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
def hello_world():
    ACCESS_TOKEN = 'EAAh51ZAZCrmYIBAHUqYn8pBlJKvJEkA2sbZBx2oQEUk4uZARv8HDtF3o91z5ZBxeS5n8FChbRZB6WsLKZCb3n3QS6yH9TGSFJIe5UPciCpqVZBmqcZBqj8y7cZCwqr5uljzZAHaVPk5yppxDwiWpX2UyTnjw6LHaq78fWf3HTRT77EIxQZDZD'
    r = find_answer("Mao trạch đông sinh năm bao nhiêu")
    return r['answer']

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
