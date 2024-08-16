from flask import Blueprint

firm_bp = Blueprint('firms', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
