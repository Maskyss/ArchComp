from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)

tasks = [
    {"id": 1,
     "title": "Simple task",
     "done": False,
     "day": 1,
     "month": 1,
     "year": 2019}
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
