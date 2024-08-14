from flask import Blueprint

sensor_bp = Blueprint('sensor', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
