from flask import Blueprint, request, flash, render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    user = User.query.filter_by(name="name").first()
    if user:
        if check_password_hash(user.password, password="pass"):
            pass
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup')
def signup():
    user = User("email", "name", "surname", password=generate_password_hash("password", method='sha256'))
    db.session.add(user)
    return "<p>signup</p>"