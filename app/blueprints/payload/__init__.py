from flask import Blueprint

payload_bp = Blueprint('payload', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
