from flask import Blueprint, render_template
from ...models import Missione
from . import mission_bp  # Importa il blueprint definito in __init__.py

@mission_bp.route('/missions')
def missions():
    missions = Missione.query.all()
    return render_template('missions.html', missions=missions)
