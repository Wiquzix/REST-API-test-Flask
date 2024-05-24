from flask import Flask, render_template, request, redirect, jsonify, json
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from instance.DataBase import *

api = Api()
app = Flask(__name__)
app.secret_key = '79d77d1e7f9348c59a384d4376a9e53f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db.init_app(app)

uri = '/todo/api/v1.0/task/'

class Main(Resource):
  def get(self,id):
    if id==0:
      tasks = Task.query.all()
      task_list = [{'id': task.id,'title': task.title, 'description': task.description, \
        'done':task.done} for task in tasks]
      return {'tasks': task_list}  
    task = Task.query.filter_by(id=id).first()
    return {'id': task.id, 'title':task.title, 'description': task.description, 'done': task.done}
  
  def post(self,id):
    task_data = request.get_json()
    if not task_data:
      return {'message': 'No input data provided'}, 400
    description = task_data.get('description')
    title = task_data.get('title')
    if not description:
      print(description)
      return {'message': 'Description is required'}, 400
    if not title:
      return {'message': 'Title is required'}, 400
    new_task = Task(title=title,description=description, done=False)
    db.session.add(new_task)
    db.session.commit()
    return {'message': 'Task added', 'task': {'id': new_task.id, 'title':new_task.title, 'description': new_task.description}}, 200

  
  def put(self,id):
    task = Task.query.get(id)
    task_data = request.get_json()
    
    if not task_data:
      return {'message': 'No input data provided'}, 400
    description = task_data.get('description')
    title = task_data.get('title')
    if not description and not title:
      return {'message': 'Description and title is required'}, 400
    if title:
      task.title=title
    if description:
      task.description=description
    db.session.commit()
    return {'message': 'Task edit', 'task': {'id': task.id, 'title':task.title,\
      'description': task.description}}, 200
    
  def delete(self,id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return 'success'
  
api.add_resource(Main, uri+'<int:id>')
api.init_app(app)

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(port=5000,debug=True)
  
  