from flask import Blueprint

motor_bp = Blueprint('motor', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
