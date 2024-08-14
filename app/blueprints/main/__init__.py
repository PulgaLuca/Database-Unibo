from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
