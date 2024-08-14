from flask import Blueprint, render_template
from ...models import Sensore
from . import sensor_bp  # Importa il blueprint definito in __init__.py

@sensor_bp.route('/sensors', methods=['GET', 'POST'])
def sensors():
    return render_template('home.html')
