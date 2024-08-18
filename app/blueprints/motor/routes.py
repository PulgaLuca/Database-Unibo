from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Motore
from . import motor_bp  # Importa il blueprint definito in __init__.py
from app import db
from ..auth.routes import login_required

@motor_bp.route('/motors', methods=['GET', 'POST'])
@login_required
def motors():
    motors = Motore.query.order_by(Motore.nome.asc()).all()
    print(motors)
    return render_template('motors.html', motors=motors)


@motor_bp.route('/add_motor', methods=['POST'])
@login_required
def add_motor():
    try:
        data = request.form
        nuovo_motor = Motore(
            nome=data['new_nome'],
            produttore=data['produttore'],
            massa=data['massa'],
            spinta=data['spinta'],
            impulso=data['impulso'],
            link=data['link'],
        )
        db.session.add(nuovo_motor)
        db.session.commit()
        flash('Motore aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del motor: {str(e)}', 'danger')
    return redirect(url_for('motor.motors'))


@motor_bp.route('/edit_motor', methods=['POST'])
@login_required
def edit_motor():
    try:
        data = request.form
        old_nome = Motore.query.get(data['old_nome'])
        
        if old_nome:
            # Modifica il record esistente
            old_nome.id = data['new_nome']
            old_nome.produttore = data['produttore']
            old_nome.massa = data['massa']
            old_nome.spinta = data['spinta']
            old_nome.impulso = data['impulso']
            old_nome.link = data['link']
            db.session.commit()
            flash('Motore modificato con successo!', 'success')
        else:
            flash('Motore non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del motor: {str(e)}', 'danger')
    
    return redirect(url_for('motor.motors'))


@motor_bp.route('/remove_motor', methods=['POST'])
@login_required
def remove_motor():
    try:
        nome = request.form['new_nome']
        motor = Motore.query.get(nome)
        if motor:
            db.session.delete(motor)
            db.session.commit()
            flash('Motore rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del motor: {str(e)}', 'danger')
    return redirect(url_for('motor.motors'))
