from flask import Blueprint

mission_bp = Blueprint('mission', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
