from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Luogo
from . import location_bp  # Importa il blueprint definito in __init__.py
from app import db

@location_bp.route('/locations', methods=['GET', 'POST'])
def locations():
    locations = Luogo.query.order_by(Luogo.id.asc()).all()
    print(locations)
    return render_template('locations.html', locations=locations)


@location_bp.route('/add_location', methods=['POST'])
def add_location():
    try:
        data = request.form
        nuovo_location = Luogo(
            id=data['new_id'],
            stato=data['stato'],
            regione=data['regione'],
            citta=data['citta'],
            via=data['via'],
            civico=data['civico'],
        )
        db.session.add(nuovo_location)
        db.session.commit()
        flash('Luogo aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del location: {str(e)}', 'danger')
    return redirect(url_for('location.locations'))


@location_bp.route('/edit_location', methods=['POST'])
def edit_location():
    try:
        data = request.form
        old_id = Luogo.query.get(data['old_id'])
        
        if old_id:
            # Modifica il record esistente
            old_id.id = data['new_id']
            old_id.stato = data['stato']
            old_id.regione = data['regione']
            old_id.citta = data['citta']
            old_id.via = data['via']
            old_id.civico = data['civico']
            db.session.commit()
            flash('Luogo modificato con successo!', 'success')
        else:
            flash('Luogo non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del location: {str(e)}', 'danger')
    
    return redirect(url_for('location.locations'))


@location_bp.route('/remove_location', methods=['POST'])
def remove_location():
    try:
        nome = request.form['new_id']
        location = Luogo.query.get(nome)
        if location:
            db.session.delete(location)
            db.session.commit()
            flash('Luogo rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del location: {str(e)}', 'danger')
    return redirect(url_for('location.locations'))
