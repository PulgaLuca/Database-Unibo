from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from ...models import DatoSensore, Missione, Sensore
from . import dashboard_bp  # Importa il blueprint definito in __init__.py
from app import db
from flask import jsonify
from ..auth.routes import login_required


@dashboard_bp.route('/data', methods=['GET', 'POST'])
@login_required
def dashboard():
    dashboard = DatoSensore.query.order_by(DatoSensore.id.asc()).all()
    missions = Missione.query.order_by(Missione.id.asc()).all()
    return render_template('dashboard.html', dashboard=dashboard, missions=missions)

@dashboard_bp.route('/missions')
@login_required
def get_missions():
    missions = Missione.query.all()
    return jsonify([{
        'id': missione.id,
        'nome': missione.nome
    } for missione in missions])


@dashboard_bp.route('/data/<int:mission_id>')
@login_required
def get_data(mission_id):
    data = DatoSensore.query.filter_by(idMissione=mission_id).all()
    return jsonify([{
        'valore': dato.valore,
        'timestamp': dato.timestamp,
        'nomeSensore': dato.nomeSensore
    } for dato in data])
