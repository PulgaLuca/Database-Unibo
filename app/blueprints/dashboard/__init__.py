from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
