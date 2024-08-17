from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from ...models import Razzo, Sensore
from . import sensor_bp  # Importa il blueprint definito in __init__.py
from app import db

@sensor_bp.route('/sensors', methods=['GET', 'POST'])
def sensors():
    sensors = Sensore.query.order_by(Sensore.nome.asc()).all()
    razzi = Razzo.query.order_by(Razzo.nome.asc()).all()
    return render_template('sensors.html', sensors=sensors, razzi=razzi)


@sensor_bp.route('/add_sensor', methods=['POST'])
def add_sensor():
    try:
        data = request.form
        nuovo_sensore = Sensore(
            nome=data['new_nome'],
            tipo=data['tipo'],
            unitaMisura=data['unitaMisura'],
            accuratezza=data['accuratezza'],
            frequenza=data['frequenza'],
            link=data['link'],
        )
        db.session.add(nuovo_sensore)
        db.session.commit()
        flash('Sensore aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del sensore: {str(e)}', 'danger')
    return redirect(url_for('sensor.sensors'))


@sensor_bp.route('/edit_sensor', methods=['POST'])
def edit_sensor():
    try:
        data = request.form
        old_nome = Sensore.query.get(data['old_nome'])
        
        if old_nome:
            # Modifica il record esistente
            old_nome.nome = data['new_nome']
            old_nome.tipo = data['tipo']
            old_nome.unitaMisura = data['unitaMisura']
            old_nome.accuratezza = data['accuratezza']
            old_nome.frequenza = data['frequenza']
            old_nome.link = data['link']
            db.session.commit()
            flash('Sensore modificato con successo!', 'success')
        else:
            flash('Sensore non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del sensore: {str(e)}', 'danger')
    
    return redirect(url_for('sensor.sensors'))


@sensor_bp.route('/remove_sensor', methods=['POST'])
def remove_sensor():
    try:
        nome = request.form['new_nome']
        sensor = Sensore.query.get(nome)
        if sensor:
            db.session.delete(sensor)
            db.session.commit()
            flash('Sensore rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del sensore: {str(e)}', 'danger')
    return redirect(url_for('sensor.sensors'))
