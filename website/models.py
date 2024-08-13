# from flask import Blueprint
# models = Blueprint('models', __name__)

from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    projects = db.relationship('Projects')

class Projects:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))