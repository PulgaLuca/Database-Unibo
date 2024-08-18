from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Paracadute
from . import parafoil_bp  # Importa il blueprint definito in __init__.py
from app import db
from ..auth.routes import login_required


@parafoil_bp.route('/parafoils', methods=['GET', 'POST'])
@login_required
def parafoils():
    parafoils = Paracadute.query.order_by(Paracadute.nome.asc()).all()
    print(parafoils)
    return render_template('parafoils.html', parafoils=parafoils)


@parafoil_bp.route('/add_parafoil', methods=['POST'])
@login_required
def add_parafoil():
    try:
        data = request.form
        nuovo_parafoil = Paracadute(
            nome=data['new_nome'],
            modello=data['modello'],
            diametro=data['diametro'],
            link=data['link'],
        )
        db.session.add(nuovo_parafoil)
        db.session.commit()
        flash('Paracadute aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del parafoil: {str(e)}', 'danger')
    return redirect(url_for('parafoil.parafoils'))


@parafoil_bp.route('/edit_parafoil', methods=['POST'])
@login_required
def edit_parafoil():
    try:
        data = request.form
        old_nome = Paracadute.query.get(data['old_nome'])
        
        if old_nome:
            # Modifica il record esistente
            old_nome.nome = data['new_nome']
            old_nome.modello = data['modello']
            old_nome.diametro = data['diametro']
            old_nome.link = data['link']
            db.session.commit()
            flash('Paracadute modificato con successo!', 'success')
        else:
            flash('Paracadute non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del parafoil: {str(e)}', 'danger')
    
    return redirect(url_for('parafoil.parafoils'))


@parafoil_bp.route('/remove_parafoil', methods=['POST'])
@login_required
def remove_parafoil():
    try:
        nome = request.form['new_nome']
        parafoil = Paracadute.query.get(nome)
        if parafoil:
            db.session.delete(parafoil)
            db.session.commit()
            flash('Paracadute rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del parafoil: {str(e)}', 'danger')
    return redirect(url_for('parafoil.parafoils'))
