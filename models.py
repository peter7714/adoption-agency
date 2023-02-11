from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

DEFAULT_IMG = 'https://o.aolcdn.com/images/dar/5845cadfecd996e0372f/23f9cc381f897ccc0fd2d464a8ab8652ee1647a6/aHR0cDovL3d3dy5ibG9nY2RuLmNvbS93b3cuam95c3RpcS5jb20vbWVkaWEvMjAwNi8xMS9waG90by1nb2VzLWhlcmUuanBn'

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    db.app = app
    db.init_app(app)
