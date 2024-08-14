from flask import Blueprint

rocket_bp = Blueprint('rocket', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
