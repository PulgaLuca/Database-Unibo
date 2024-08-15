from flask import Blueprint

location_bp = Blueprint('location', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
