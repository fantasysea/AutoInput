from app import db
import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(80), unique=True)
    time = db.Column(db.DateTime, unique=True)
    status = db.Column(db.Integer)

    def __init__(self, message,time,status=0):
        self.message = message
        self.time = time
        self.status = status


    def __repr__(self):
        return '<Todo %r>' % self.message