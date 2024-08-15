from flask import Blueprint

parafoil_bp = Blueprint('parafoil', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
