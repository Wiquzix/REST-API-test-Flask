from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)  
  description = db.Column(db.Text)
  done = db.Column(db.Boolean)