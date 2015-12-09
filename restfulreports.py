from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# basic tasks to use as data for testing
tasks = [
    {
        'id': 1234564,
        'service': u'phishing',
        'urls/ips': u'http://plaidlikedad.com, http://punlife.com',
        'done': False
    },
    {
        'id': 2123454,
        'service': u'malware',
        'urls/ips': u'http://straighttoprod.com',
        'done': False
    },
    {
        'id': 3434564,
        'service': u'network abuse',
        'urls/ips': u'127.0.0.1, 127.0.0.2, 127.0.0.3, 127.0.0.4',
        'done': False
    },
    {
        'id': 3454564,
        'service': u'spam',
        'urls/ips': u'headerinfo?, email body?',
        'done': False
    },
]

'''
curl commands:
list tasks: curl -u rayray:python -i http://localhost:5000/todo/api/v1.0/tasks
make a new task: $ curl -u rayray:python -i -H "Content-Type: application/json" -X POST -d '{"service":"phishing","id":9945499,"urls/ips":"http://punliife.com"}' http://localhost:5000/todo/api/v1.0/tasks
modify a task: curl -u rayray:python -i -H "Content-Type: application/json" -X PUT  -d '{"urls/ips":"http://punliife.com/index.html"}' http://localhost:5000/todo/api/v1.0/tasks/<int:task_id>
modify a task as complete: curl -u rayray:python -i -H "Content-Type: application/json" -X PUT  -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/<int:task_id>
delete a task: curl -u rayray:python -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1.0/tasks/<int:task_id>
'''


def make_public_task(task):
    """
    small helper function that generates a "public" version of a task to send to the client
    :param task:
    :return:
    """
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/')
def index():
    """
    home page of the flask app
    :return:
    """
    return '''My first attempt at flask and rest API - reference:
           http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask'''


@auth.get_password
def get_password(username):
    """
    http basic auth function
    this app decorator can be added to functions that should require auth
    :param username:
    :return:
    """
    if username == 'rayray':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    """
    error handling for no auth
    :return:
    """
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(404)
def not_found(error):
    """
    error handling for requests to nonexistent resources
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    """
    return list of stored tasks and their uri's for the API
    :return:
    """
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    """
    return task based on task id
    :param task_id:
    :return:
    """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():
    """
    function to create new tasks
    :return:
    """
    if not request.json or 'service' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'service': request.json['service'],
        'urls/ips': request.json.get('urls/ips', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    """
    function to update existing tasks
    :param task_id:
    :return:
    """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'service' in request.json and type(request.json['service']) != unicode:
        abort(400)
    if 'urls/ips' in request.json and type(request.json['urls/ips']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['service'] = request.json.get('service', task[0]['service'])
    task[0]['urls/ips'] = request.json.get('urls/ips', task[0]['urls/ips'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    """
    function to remove a task
    :param task_id:
    :return:
    """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
