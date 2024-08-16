from flask import Blueprint

people_bp = Blueprint('people', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
