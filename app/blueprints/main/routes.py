from flask import render_template
from . import main_bp  # Importa il blueprint definito in __init__.py

@main_bp.route('/')
def home():
    return render_template('home.html')
