from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Materiale
from . import material_bp  # Importa il blueprint definito in __init__.py
from app import db

@material_bp.route('/materials')
def materials():
    materials = Materiale.query.order_by(Materiale.nome.asc()).all()
    print(materials)
    return render_template('materials.html', materials=materials)

@material_bp.route('/add_material', methods=['POST'])
def add_material():
    try:
        data = request.form
        nuovo_materiale = Materiale(
            nome=data['new_nome'],
            note=data['note'],
        )
        db.session.add(nuovo_materiale)
        db.session.commit()
        flash('Materiale aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del materiale: {str(e)}', 'danger')
    return redirect(url_for('material.materials'))


@material_bp.route('/edit_material', methods=['POST'])
def edit_material():
    try:
        data = request.form
        old_nome = Materiale.query.get(data['old_nome'])
        
        if old_nome:
            # Modifica il record esistente
            old_nome.nome = data['new_nome']
            old_nome.note = data['note']
            db.session.commit()
            flash('Materiale modificato con successo!', 'success')
        else:
            flash('Materiale non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del materiale: {str(e)}', 'danger')
    return redirect(url_for('material.materials'))


@material_bp.route('/remove_material', methods=['POST'])
def remove_material():
    try:
        nome = request.form['new_nome']
        material = Materiale.query.get(nome)
        if material:
            db.session.delete(material)
            db.session.commit()
            flash('Materiale rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del materiale: {str(e)}', 'danger')
    return redirect(url_for('material.materials'))
