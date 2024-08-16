from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import AziendaConsulenziale, AziendaFinanziatrice, AziendaFornitrice, MissioneConsulenza, MissioneFinanziatore, MissioneFornitore
from . import firm_bp  # Importa il blueprint definito in __init__.py
from app import db

@firm_bp.route('/firms', methods=['GET', 'POST'])
def goals():
    aziende_fornitrici = AziendaFornitrice.query.order_by(AziendaFornitrice.nome.asc()).all()
    aziende_consulenziali = AziendaConsulenziale.query.order_by(AziendaConsulenziale.nome.asc()).all()
    aziende_finanziatrici = AziendaFinanziatrice.query.order_by(AziendaFinanziatrice.nome.asc()).all()
    return render_template('firms.html', aziende_fornitrici=aziende_fornitrici, aziende_consulenziali=aziende_consulenziali, aziende_finanziatrici=aziende_finanziatrici)

############################################## FINANZIATORE ##############################################

@firm_bp.route('/finanziatore_add_azienda', methods=['POST'])
def finanziatore_add_azienda():
    pass

@firm_bp.route('/finanziatore_edit_azienda', methods=['POST'])
def finanziatore_edit_azienda():
    pass

@firm_bp.route('/finanziatore_remove_azienda', methods=['POST'])
def finanziatore_remove_azienda():
    pass

############################################## FORNITORE ##############################################


@firm_bp.route('/fornitore_add_azienda', methods=['POST'])
def fornitore_add_azienda():
    pass

@firm_bp.route('/fornitore_edit_azienda', methods=['POST'])
def fornitore_edit_azienda():
    pass

@firm_bp.route('/fornitore_remove_azienda', methods=['POST'])
def fornitore_remove_azienda():
    pass


############################################## CONSULENZA ##############################################

@firm_bp.route('/consulenza_add_azienda', methods=['POST'])
def consulenza_add_azienda():
    pass

@firm_bp.route('/consulenza_edit_azienda', methods=['POST'])
def consulenza_edit_azienda():
    pass

@firm_bp.route('/consulenza_remove_azienda', methods=['POST'])
def consulenza_remove_azienda():
    pass
