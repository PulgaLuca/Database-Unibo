from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
