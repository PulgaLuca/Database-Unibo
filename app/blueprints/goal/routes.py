from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import Obiettivo
from . import goal_bp  # Importa il blueprint definito in __init__.py
from app import db
from ..auth.routes import login_required

@goal_bp.route('/goals', methods=['GET', 'POST'])
@login_required
def goals():
    goals = Obiettivo.query.order_by(Obiettivo.id.asc()).all()
    print(goals)
    return render_template('goals.html', goals=goals)


@goal_bp.route('/add_goal', methods=['POST'])
@login_required
def add_goal():
    try:
        data = request.form
        nuovo_goal = Obiettivo(
            id=data['new_id'],
            nome=data['nome'],
        )
        db.session.add(nuovo_goal)
        db.session.commit()
        flash('Obiettivo aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del goal: {str(e)}', 'danger')
    return redirect(url_for('goal.goals'))


@goal_bp.route('/edit_goal', methods=['POST'])
@login_required
def edit_goal():
    try:
        data = request.form
        old_id = Obiettivo.query.get(data['old_id'])
        
        if old_id:
            # Modifica il record esistente
            old_id.id = data['new_id']
            old_id.nome = data['nome']
            db.session.commit()
            flash('Obiettivo modificato con successo!', 'success')
        else:
            flash('Obiettivo non trovato!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del goal: {str(e)}', 'danger')
    
    return redirect(url_for('goal.goals'))


@goal_bp.route('/remove_goal', methods=['POST'])
@login_required
def remove_goal():
    try:
        nome = request.form['new_id']
        goal = Obiettivo.query.get(nome)
        if goal:
            db.session.delete(goal)
            db.session.commit()
            flash('Obiettivo rimosso con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del goal: {str(e)}', 'danger')
    return redirect(url_for('goal.goals'))
