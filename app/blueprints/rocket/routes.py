from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Razzo, Motore, Paracadute, Materiale
from . import rocket_bp  # Importa il blueprint definito in __init__.py
from app import db

@rocket_bp.route('/rockets')
def rockets():
    razzi = Razzo.query.all()
    motori = Motore.query.all()
    paracaduti = Paracadute.query.all()
    materiali = Materiale.query.all()
    return render_template('rockets.html', razzi=razzi, motori=motori, paracaduti=paracaduti, materiali=materiali)


@rocket_bp.route('/add_rocket', methods=['POST'])
def add_rocket():
    try:
        data = request.form
        nuovo_razzo = Razzo(
            nome=data['nome'],
            massa=data['massa'],
            lunghezza=data['lunghezza'],
            larghezza=data['larghezza'],
            altezza=data['altezza'],
            link=data['link'],
            nomeMotore=data['nomeMotore'],
            nomeParacadute=data['nomeParacadute'],
            nomeMateriale=data['nomeMateriale']
        )
        db.session.add(nuovo_razzo)
        db.session.commit()
        flash('Razzo aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del razzo: {str(e)}', 'danger')
    return redirect(url_for('rocket.rockets'))


@rocket_bp.route('/edit_rocket', methods=['POST'])
def edit_rocket():
    try:
        data = request.form
        razzo = Razzo.query.filter_by(
            nome=data['old_nome'],
            nomeMotore=data['old_nomeMotore'],
            nomeParacadute=data['old_nomeParacadute'],
            nomeMateriale=data['old_nomeMateriale']
        ).first()

        if razzo:
            razzo.massa = data['massa']
            razzo.lunghezza = data['lunghezza']
            razzo.larghezza = data['larghezza']
            razzo.altezza = data['altezza']
            razzo.link = data['link']
            razzo.nomeMotore = data['nomeMotore']
            razzo.nomeParacadute = data['nomeParacadute']
            razzo.nomeMateriale = data['nomeMateriale']
            db.session.commit()
            flash('Razzo modificato con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del razzo: {str(e)}', 'danger')
    return redirect(url_for('rocket.rockets'))


@rocket_bp.route('/remove_rocket', methods=['POST'])
def remove_rocket():
    try:        
        data = request.form
        razzo = Razzo.query.filter_by(
            nome=data['nome'],
            nomeMotore=data['nomeMotore'],
            nomeParacadute=data['nomeParacadute'],
            nomeMateriale=data['nomeMateriale']
        ).first()

        if razzo:
            db.session.delete(razzo)
            db.session.commit()
            flash('Razzo rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del razzo: {str(e)}', 'danger')
    return redirect(url_for('rocket.rockets'))
