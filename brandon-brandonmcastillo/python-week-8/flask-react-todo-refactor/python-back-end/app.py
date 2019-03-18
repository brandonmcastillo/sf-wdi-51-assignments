import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
# Set Base Directory
# Debug tells the env to check for errors
DEBUG = True
PORT = 8000
# 'baseddir' is the current directory
# os is a python thing
basedir = os.path.abspath(os.path.dirname(__file__))
# Setup Database
# Instead of running on a server, we are creating a serverless database that is a file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.reacttodo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Init Marshmallow
marshmallow = Marshmallow(app)


#Todo Routes
@app.route('/todo', methods=['POST', 'GET'])
@app.route('/todo/<todoid>', methods=['GET', 'DELETE', 'PUT'])
# Get All or Create A Todo
def get_create_todo(todoid=None):
    from models import Todo
    if todoid == None and request.method == 'GET':
        return Todo.get_all_todos()
    elif todoid == None and request.method == 'POST':
        body = request.json['body']
        priority = request.json['priority']
        completed = request.json['completed']
        return Todo.create_todo(body, priority, completed)
    elif todoid and request.method == 'PUT':
        body = request.json['body']
        priority = request.json['priority']
        completed = request.json['completed']
        return Todo.update_todo(todoid, body, priority, completed)
    elif todoid and request.method == 'DELETE':
        return Todo.delete_todo(todoid)
    else:
        return Todo.get_todo(todoid)


# Update a To Do


@app.route('/')
def hello_world():
    return 'Hello World'


# if __name__ is equal to main, run (initialize)
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
