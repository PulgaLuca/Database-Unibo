from flask import render_template
from . import main_bp  # Importa il blueprint definito in __init__.py
from ..auth.routes import login_required

@main_bp.route('/')
@login_required
def home():
    return render_template('home.html')
