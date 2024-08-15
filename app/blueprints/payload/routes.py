from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Payload
from . import payload_bp  # Importa il blueprint definito in __init__.py
from app import db

@payload_bp.route('/payloads', methods=['GET', 'POST'])
def payloads():
    payloads = Payload.query.order_by(Payload.id.asc()).all()
    print(payloads)
    return render_template('payloads.html', payloads=payloads)


@payload_bp.route('/add_payload', methods=['POST'])
def add_payload():
    try:
        data = request.form
        nuovo_payload = Payload(
            id=data['new_id'],
            nome=data['nome'],
            massa=data['massa'],
            larghezza=data['larghezza'],
            lunghezza=data['lunghezza'],
            altezza=data['altezza'],
        )
        db.session.add(nuovo_payload)
        db.session.commit()
        flash('Payload aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del payload: {str(e)}', 'danger')
    return redirect(url_for('payload.payloads'))


@payload_bp.route('/edit_payload', methods=['POST'])
def edit_payload():
    try:
        data = request.form
        old_id = Payload.query.get(data['old_id'])
        
        if old_id:
            # Modifica il record esistente
            old_id.id = data['new_id']
            old_id.nome = data['nome']
            old_id.massa = data['massa']
            old_id.larghezza = data['larghezza']
            old_id.lunghezza = data['lunghezza']
            old_id.altezza = data['altezza']
            db.session.commit()
            flash('Payload modificato con successo!', 'success')
        else:
            flash('Payload non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del payload: {str(e)}', 'danger')
    
    return redirect(url_for('payload.payloads'))


@payload_bp.route('/remove_payload', methods=['POST'])
def remove_payload():
    try:
        nome = request.form['new_id']
        payload = Payload.query.get(nome)
        if payload:
            db.session.delete(payload)
            db.session.commit()
            flash('Payload rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del payload: {str(e)}', 'danger')
    return redirect(url_for('payload.payloads'))
