from datetime import datetime
from ...models import Missione, Luogo, Payload, Razzo, MissioneObiettivo, Obiettivo
from . import mission_bp  # Importa il blueprint definito in __init__.py
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from app import db
from ..auth.routes import login_required


@mission_bp.route('/missions')
@login_required
def missions():
    missioni = Missione.query.order_by(Missione.id.asc()).all()
    luoghi = Luogo.query.order_by(Luogo.id.asc()).all()
    payloads = Payload.query.order_by(Payload.id.asc()).all()
    razzi = Razzo.query.order_by(Razzo.nome.asc()).all()
    obiettivi = Obiettivo.query.order_by(Obiettivo.nome.asc()).all()
    return render_template('mission.html', missioni=missioni, luoghi=luoghi, payloads=payloads, razzi=razzi, obiettivi=obiettivi)


@mission_bp.route('/add_mission', methods=['POST'])
@login_required
def add_mission():
    try:
        data = request.form
        data_inizio = datetime.strptime(data['mission-dataLancio'], '%Y-%m-%d').date()
        
        nuova_missione = Missione(
            nome=data['mission-nome'],
            dataLancio=data_inizio,
            stato=data['mission-stato'],
            idLuogo=int(data['mission-idLuogo']),
            idPayload=int(data['mission-idPayload']),
            nomeRazzo=data['mission-nomeRazzo']
        )
        db.session.add(nuova_missione)
        db.session.commit()
        flash('Missione aggiunta con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta della missione: {str(e)}', 'danger')
    return redirect(url_for('mission.missions'))


@mission_bp.route('/edit_mission', methods=['POST'])
@login_required
def edit_mission():
    try:
        data = request.form
        print(data)
        missione = Missione.query.filter_by(
            id=data['old-mission-id'],
            idPayload=int(data['old-mission-idPayload']),
            idLuogo=data['old-mission-idLuogo'],
            nomeRazzo=data['old-mission-nomeRazzo']
        ).first()

        if missione:
            missione.nome = data['mission-nome']
            missione.dataLancio = datetime.strptime(data['mission-dataLancio'], '%Y-%m-%d').date()
            missione.stato = data['mission-stato']
            missione.idLuogo = int(data['mission-idLuogo'])
            missione.idPayload = int(data['mission-idPayload'])
            missione.nomeRazzo = data['mission-nomeRazzo']
            db.session.commit()
            flash('Missione modificata con successo!', 'success')
        else:
            flash('Missione non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica della missione: {str(e)}', 'danger')    
    return redirect(url_for('mission.missions'))


@mission_bp.route('/remove_mission', methods=['POST'])
@login_required
def remove_mission():
    try:
        data = request.form
        missione = Missione.query.filter_by(
            id=data['old-mission-id'],
            idPayload=data['mission-idPayload'],
            idLuogo=data['mission-idLuogo'],
            nomeRazzo=data['mission-nomeRazzo']
        ).first()
        if missione:
            db.session.delete(missione)
            db.session.commit()
            flash('Missione rimossa con successo!', 'success')
        else:
            flash('Missione non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione della missione: {str(e)}', 'danger')
    return redirect(url_for('mission.missions'))


############################################## TEST ##############################################

@mission_bp.route('/get_obiettivi/<idMissione>', methods=['GET'])
@login_required
def get_obiettivi(idMissione):
    obiettivi = MissioneObiettivo.query.filter_by(idMissione=idMissione).all()
    obiettivi_dict = [{"nome": obiettivo.idObiettivo} for obiettivo in obiettivi]
    print(obiettivi_dict)
    return jsonify(obiettivi_dict)


@mission_bp.route('/add_obiettivo', methods=['POST'])
@login_required
def add_obiettivo():
    data = request.get_json()
    nome_missione = data.get('idMissione')
    nome_obiettivo = data.get('idObiettivo')
    
    if nome_missione and nome_obiettivo:
        nuovo_obiettivo = MissioneObiettivo(idMissione=nome_missione, idObiettivo=nome_obiettivo)
        db.session.add(nuovo_obiettivo)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})


@mission_bp.route('/remove_obiettivo', methods=['POST'])
@login_required
def remove_obiettivo():
    data = request.get_json()
    nome_missione = data.get('idMissione')
    nome_obiettivo = data.get('idObiettivo')
    
    if nome_missione and nome_obiettivo:
        obiettivo_da_rimuovere = MissioneObiettivo.query.filter_by(idMissione=nome_missione, idObiettivo=nome_obiettivo).first()
        if obiettivo_da_rimuovere:
            db.session.delete(obiettivo_da_rimuovere)
            db.session.commit()
            return jsonify({'success': True})
    return jsonify({'success': False})
