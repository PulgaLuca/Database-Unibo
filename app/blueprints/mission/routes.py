from ...models import Missione
from . import mission_bp  # Importa il blueprint definito in __init__.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db

@mission_bp.route('/missions')
def missions():
    missions = Missione.query.order_by(Missione.id.asc()).all()
    print(missions)
    return render_template('missions.html', missions=missions)

@mission_bp.route('/add_mission', methods=['POST'])
def add_mission():
    try:
        data = request.form
        nuovo_missione = Missione(
            nome=data['new_nome'],
            note=data['note'],
        )
        db.session.add(nuovo_missione)
        db.session.commit()
        flash('Missione aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del missione: {str(e)}', 'danger')
    return redirect(url_for('mission.missions'))


@mission_bp.route('/edit_mission', methods=['POST'])
def edit_mission():
    try:
        data = request.form
        old_razzo = Missione.query.get(data['old_nome'])
        
        if old_razzo:
            # Modifica il record esistente
            old_razzo.nome = data['new_nome']
            old_razzo.note = data['note']
            db.session.commit()
            flash('Missione modificato con successo!', 'success')
        else:
            flash('Missione non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del missione: {str(e)}', 'danger')
    
    return redirect(url_for('mission.missions'))


@mission_bp.route('/remove_mission', methods=['POST'])
def remove_mission():
    try:
        nome = request.form['new_nome']
        mission = Missione.query.get(nome)
        if mission:
            db.session.delete(mission)
            db.session.commit()
            flash('Missione rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del missione: {str(e)}', 'danger')
    return redirect(url_for('mission.missions'))
