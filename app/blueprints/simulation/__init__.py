from flask import Blueprint

simulation_bp = Blueprint('simulation', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
