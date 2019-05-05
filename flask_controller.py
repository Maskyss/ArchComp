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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'ServerPart': 'Yasenko'},
                                 {'UiPart': 'Sirenko'},
                                 {'TestPart': 'Antoniuk'}), 404)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': tasks})


@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': request.json['done'],
        'day': request.json['day'],
        'month': request.json['month'],
        'year': request.json['year']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
