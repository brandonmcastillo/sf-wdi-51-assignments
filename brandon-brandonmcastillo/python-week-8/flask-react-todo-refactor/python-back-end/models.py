from app import db, marshmallow
from flask import jsonify


class Todo(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, body, priority, completed):
        self.body = body
        self.priority = priority
        self.completed = completed

    @classmethod
    def get_todo(cls, todoid):
        todo = Todo.query.get(todoid)
        return todo_schema.jsonify(todo)

    # Get All Todos
    @classmethod
    def get_all_todos(cls):
        todos = Todo.query.all()
        return todos_schema.jsonify(todos)

    #Create A Todo
    @classmethod
    def create_todo(cls, body, priority, completed):
        new_todo = Todo(body, priority, completed)
        try:
            db.session.add(new_todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return todo_schema.jsonify(new_todo)

    # Delete Todo
    @classmethod
    def delete_todo(cls, todoid):
        delete_todo = Todo.query.get(todoid)
        try:
            db.session.delete(delete_todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception('Session rollback')
        return todo_schema.jsonify(delete_todo)

    # Update Todo
    @classmethod
    def update_todo(cls, todoid, body, priority, completed):
        todo = Todo.query.get(todoid)
        todo.body = body
        todo.priority = priority
        todo.completed = completed
        db.session.commit()
        return todo_schema.jsonify(todo)


class TodoSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'body', 'priority', 'completed')


todo_schema = TodoSchema(strict=True)
todos_schema = TodoSchema(many=True, strict=True)

if __name__ == 'models':
    db.create_all() 