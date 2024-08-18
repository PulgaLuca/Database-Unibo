from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
