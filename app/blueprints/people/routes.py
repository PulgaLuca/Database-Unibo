from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from datetime import datetime
from ...models import Membro, Ruolo, Team, Dipartimento, Incarico
from . import people_bp  # Importa il blueprint definito in __init__.py
from app import db
from ..auth.routes import login_required


@people_bp.route('/manage_people', methods=['GET', 'POST'])
@login_required
def manage_people():
    membri = Membro.query.all()
    ruoli = Ruolo.query.all()
    dipartimenti = Dipartimento.query.all()
    teams = Team.query.all()
    incarichi = Incarico.query.all()
    return render_template('people.html', membri=membri, ruoli=ruoli, dipartimenti=dipartimenti, teams=teams, incarichi=incarichi)

##########################################################  MEMBRO  ######################################################################################

@people_bp.route('/add_member', methods=['POST'])
@login_required
def add_member():
    try:
        data = request.form
        hashed_password = generate_password_hash(data['membro-password'])
        nuovo_membro = Membro(
            nome=data['membro-nome'],
            cognome=data['membro-cognome'],
            email=data['membro-email'],
            password=hashed_password,
        )
        db.session.add(nuovo_membro)
        db.session.commit()
        flash('Membro aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del membro: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/edit_member', methods=['POST'])
@login_required
def edit_member():
    try:
        data = request.form
        membro = Membro.query.get(data['membro-id'])
        if membro:
            membro.nome = data['membro-nome']
            membro.cognome = data['membro-cognome']
            membro.email = data['membro-email']
            membro.password = data['membro-password']
            db.session.commit()
            flash('Membro modificato con successo!', 'success')
        else:
            flash('Membro non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del membro: {str(e)}', 'danger')    
    return redirect(url_for('people.manage_people'))


@people_bp.route('/remove_member', methods=['POST'])
@login_required
def remove_member():
    try:
        data = request.form
        membro = Membro.query.get(data['membro-id'])
        
        if membro:
            db.session.delete(membro)
            db.session.commit()
            flash('Membro rimosso con successo!', 'success')
        else:
            flash('Membro non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del membro: {str(e)}', 'danger')
    
    return redirect(url_for('people.manage_people'))

##############################################################  RUOLO  ##################################################################################

@people_bp.route('/add_role', methods=['POST'])
@login_required
def add_role():
    try:
        data = request.form
        nuovo_ruolo = Ruolo(
            nome=data['ruolo-nome'],
        )
        db.session.add(nuovo_ruolo)
        db.session.commit()
        flash('Ruolo aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del ruolo: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/edit_role', methods=['POST'])
@login_required
def edit_role():
    try:
        data = request.form
        ruolo = Ruolo.query.get(data['old_name_ruolo'])
        if ruolo:
            ruolo.nome = data['ruolo-nome']
            db.session.commit()
            flash('Ruolo modificato con successo!', 'success')
        else:
            flash('Ruolo non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del ruolo: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/remove_role', methods=['POST'])
@login_required
def remove_role():
    try:
        data = request.form
        ruolo = Ruolo.query.get(data['ruolo-nome'])
        if ruolo:
            db.session.delete(ruolo)
            db.session.commit()
            flash('Ruolo rimosso con successo!', 'success')
        else:
            flash('Ruolo non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del ruolo: {str(e)}', 'danger')
    
    return redirect(url_for('people.manage_people'))

##############################################################  TEAM  ##################################################################################

@people_bp.route('/add_team', methods=['POST'])
@login_required
def add_team():
    try:
        data = request.form
        team = Team(
            nome=data['team-nome'],
            nomeDipartimento=data['team-nomedipartimento']
        )
        db.session.add(team)
        db.session.commit()
        flash('Team aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del team: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/edit_team', methods=['POST'])
@login_required
def edit_team():
    try:
        data = request.form
        team = Team.query.get(data['old_name_team'])
        if team:
            team.nome = data['team-nome']
            db.session.commit()
            flash('Team modificato con successo!', 'success')
        else:
            flash('Team non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del team: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/remove_team', methods=['POST'])
@login_required
def remove_team():
    try:
        data = request.form
        team = Team.query.get(data['team-nome'])
        if team:
            db.session.delete(team)
            db.session.commit()
            flash('Team rimosso con successo!', 'success')
        else:
            flash('Team non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del team: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))

##############################################################  DIPARTIMENTO  ##################################################################################

@people_bp.route('/add_department', methods=['POST'])
@login_required
def add_department():
    try:
        data = request.form
        dipartimento = Dipartimento(
            nome=data['dipartimento-nome'],
        )
        db.session.add(dipartimento)
        db.session.commit()
        flash('Dipartimento aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta del dipartimento: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/edit_department', methods=['POST'])
@login_required
def edit_department():
    try:
        data = request.form
        dipartimento = Dipartimento.query.get(data['old_name_dipartimento'])
        if dipartimento:
            dipartimento.nome = data['dipartimento-nome']
            db.session.commit()
            flash('Dipartimento modificato con successo!', 'success')
        else:
            flash('Dipartimento non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica del dipartimento: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/remove_department', methods=['POST'])
@login_required
def remove_department():
    try:
        data = request.form
        dep = Dipartimento.query.get(data['dipartimento-nome'])
        if dep:
            db.session.delete(dep)
            db.session.commit()
            flash('Dipartimento rimosso con successo!', 'success')
        else:
            flash('Dipartimento non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione del dipartimento: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))

##############################################################  INCARICO  ##################################################################################

@people_bp.route('/add_chore', methods=['POST'])
@login_required
def add_chore():
    try:
        data = request.form

        data_inizio = datetime.strptime(data['incarico-dataInizio'], '%Y-%m-%d').date()
        data_fine = data.get('incarico-dataFine') # Could be NULL
        if data_fine:
            data_fine = datetime.strptime(data_fine, '%Y-%m-%d').date()
        else:
            data_fine = None

        nuovo_incarico = Incarico(
            dataInizio=data_inizio,
            dataFine=data_fine,
            nomeTeam=data['incarico-nomeTeam'],
            idMembro=int(data['incarico-idMembro']),
            nomeRuolo=data['incarico-nomeRuolo']
        )
        db.session.add(nuovo_incarico)
        db.session.commit()
        flash('Incarico aggiunto con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta dell\'incarico: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))


@people_bp.route('/edit_chore', methods=['POST'])
@login_required
def edit_chore():
    try:
        data = request.form

        data_inizio = datetime.strptime(data['old-incarico-dataInizio'], '%Y-%m-%d').date()
        data_fine = data.get('incarico-dataFine') # Could be NULL
        if data_fine:
            data_fine = datetime.strptime(data_fine, '%Y-%m-%d').date()
        else:
            data_fine = None

        incarico = Incarico.query.filter_by(
            dataInizio=data_inizio,
            nomeTeam=data['old-incarico-nomeTeam'],
            idMembro=int(data['old-incarico-idMembro']),
            nomeRuolo=data['old-incarico-nomeRuolo']
        ).first()
        if incarico:
            incarico.dataInizio = data_inizio
            incarico.dataFine = data_fine
            incarico.nomeTeam = data['incarico-nomeTeam']
            incarico.idMembro = data['incarico-idMembro']
            incarico.nomeRuolo = data['incarico-nomeRuolo']
            db.session.commit()
            flash('Incarico modificato con successo!', 'success')
        else:
            flash('Incarico non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica dell\'incarico: {str(e)}', 'danger')    
    return redirect(url_for('people.manage_people'))


@people_bp.route('/remove_chore', methods=['POST'])
@login_required
def remove_chore():
    try:
        data = request.form

        data_inizio = datetime.strptime(data['incarico-dataInizio'], '%Y-%m-%d').date()
        data_fine = data.get('incarico-dataFine') # Could be NULL
        if data_fine:
            data_fine = datetime.strptime(data_fine, '%Y-%m-%d').date()
        else:
            data_fine = None

        incarico = Incarico.query.filter_by(
            dataInizio=data_inizio,
            nomeTeam=data['incarico-nomeTeam'],
            idMembro=data['incarico-idMembro'],
            nomeRuolo=data['incarico-nomeRuolo']
        ).first()
        if incarico:
            db.session.delete(incarico)
            db.session.commit()
            flash('Incarico rimosso con successo!', 'success')
        else:
            flash('Incarico non trovato.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione dell\'incarico: {str(e)}', 'danger')
    return redirect(url_for('people.manage_people'))
