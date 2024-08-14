from flask import Blueprint

material_bp = Blueprint('material', __name__)

from . import routes  # Importa il modulo routes che conterrà le route per il blueprint
