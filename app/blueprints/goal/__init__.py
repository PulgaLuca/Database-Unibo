from flask import Blueprint

goal_bp = Blueprint('goal', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
