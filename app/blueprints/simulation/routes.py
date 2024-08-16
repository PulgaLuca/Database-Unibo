from ...models import Simulazione, Team, Razzo
from . import simulation_bp  # Importa il blueprint definito in __init__.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db


@simulation_bp.route('/simulations')
def simulations():
    simulazioni = Simulazione.query.all()
    teams = Team.query.all()
    razzi = Razzo.query.all()
    return render_template('simulations.html', simulazioni=simulazioni, razzi=razzi, teams=teams)


@simulation_bp.route('/add_simulation', methods=['POST'])
def add_simulazione():
    try:
        data = request.form
        nuova_simulazione = Simulazione(
            id=data['id'],
            nome=data['nome'],
            link=data['link'],
            nomeTeam=data['nomeTeam'],
            nomeRazzo=data['nomeRazzo']
        )
        db.session.add(nuova_simulazione)
        db.session.commit()
        flash('Simulazione aggiunta con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta della simulazione: {str(e)}', 'danger')
    return redirect(url_for('simulation.simulations'))


@simulation_bp.route('/edit_simulation', methods=['POST'])
def edit_simulazione():
    try:
        data = request.form
        simulazione = Simulazione.query.filter_by(
            id=data['old_id'],
            nomeTeam=data['old_nomeTeam'],
            nomeRazzo=data['old_nomeRazzo']
        ).first()
        if simulazione:
            simulazione.id = data['id']
            simulazione.nome = data['nome']
            simulazione.link = data['link']
            simulazione.nomeTeam = data['nomeTeam']
            simulazione.nomeRazzo = data['nomeRazzo']
            db.session.commit()
            flash('Simulazione modificata con successo!', 'success')
        else:
            flash('Simulazione non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica della simulazione: {str(e)}', 'danger')
    return redirect(url_for('simulation.simulations'))


@simulation_bp.route('/remove_simulation', methods=['POST'])
def remove_simulazione():
    try:
        data = request.form
        simulazione = Simulazione.query.filter_by(
            id=data['id'],
            nomeTeam=data['nomeTeam'],
            nomeRazzo=data['nomeRazzo']
        ).first()
        if simulazione:
            db.session.delete(simulazione)
            db.session.commit()
            flash('Simulazione rimossa con successo!', 'success')
        else:
            flash('Simulazione non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione della simulazione: {str(e)}', 'danger')
    return redirect(url_for('simulation.simulations'))
