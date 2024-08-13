from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@views.route('/home', methods=['GET'])
def home():
    return render_template("home.html")