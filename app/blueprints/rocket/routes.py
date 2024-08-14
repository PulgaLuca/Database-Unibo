from flask import Blueprint, render_template
from ...models import Razzo
from . import rocket_bp  # Importa il blueprint definito in __init__.py



@rocket_bp.route('/rockets')
def rockets():
    return render_template('home.html')