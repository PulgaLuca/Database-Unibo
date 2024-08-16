from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from ...models import AziendaConsulenziale, AziendaFinanziatrice, AziendaFornitrice, MissioneConsulenza, MissioneFinanziatore, MissioneFornitore, Missione
from . import firm_bp  # Importa il blueprint definito in __init__.py
from app import db


@firm_bp.route('/firms', methods=['GET', 'POST'])
def firms():
    aziende_fornitrici = AziendaFornitrice.query.order_by(AziendaFornitrice.nome.asc()).all()
    aziende_consulenziali = AziendaConsulenziale.query.order_by(AziendaConsulenziale.nome.asc()).all()
    aziende_finanziatrici = AziendaFinanziatrice.query.order_by(AziendaFinanziatrice.nome.asc()).all()
    return render_template('firms.html', aziende_fornitrici=aziende_fornitrici, aziende_consulenziali=aziende_consulenziali, aziende_finanziatrici=aziende_finanziatrici)

############################################## FINANZIATORE ##############################################

@firm_bp.route('/finanziatore_add_azienda', methods=['POST'])
def finanziatore_add_azienda():
    try:
        data = request.form
        azienda = AziendaFinanziatrice(
            importo=data['azienda-importo-finanziatrice'],
            nome=data['azienda-nome-finanziatrice'],
            note=data['azienda-note-finanziatrice'],
            link=data['azienda-link-finanziatrice'],
        )
        db.session.add(azienda)
        db.session.commit()
        flash('Azienda aggiunta con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/finanziatore_edit_azienda', methods=['POST'])
def finanziatore_edit_azienda():
    try:
        data = request.form
        old_nome = AziendaFinanziatrice.query.get(data['old_name_azienda_finanziatrice'])
        
        if old_nome:
            old_nome.nome = data['azienda-nome-finanziatrice']
            old_nome.note = data['azienda-note-finanziatrice']
            old_nome.link = data['azienda-link-finanziatrice']
            old_nome.importo = data['azienda-importo-finanziatrice']
            db.session.commit()
            flash('Azienda modificata con successo!', 'success')
        else:
            flash('Azienda non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/finanziatore_remove_azienda', methods=['POST'])
def finanziatore_remove_azienda():
    try:
        nome = request.form['azienda-nome-finanziatrice']
        material = AziendaFinanziatrice.query.get(nome)
        if material:
            db.session.delete(material)
            db.session.commit()
            flash('Azienda rimossa con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


############################################## FORNITORE ##############################################

@firm_bp.route('/fornitore_add_azienda', methods=['POST'])
def fornitore_add_azienda():
    try:
        data = request.form
        azienda = AziendaFornitrice(
            quantita=data['azienda-quantita-fornitrice'],
            nome=data['azienda-nome-fornitrice'],
            note=data['azienda-note-fornitrice'],
            link=data['azienda-link-fornitrice'],
        )
        db.session.add(azienda)
        db.session.commit()
        flash('Azienda aggiunta con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/fornitore_edit_azienda', methods=['POST'])
def fornitore_edit_azienda():
    try:
        data = request.form
        old_nome = AziendaFornitrice.query.get(data['old_name_azienda_fornitrice'])
        
        if old_nome:
            old_nome.nome = data['azienda-nome-fornitrice']
            old_nome.note = data['azienda-note-fornitrice']
            old_nome.link = data['azienda-link-fornitrice']
            old_nome.quantita = data['azienda-quantita-fornitrice']
            db.session.commit()
            flash('Azienda modificata con successo!', 'success')
        else:
            flash('Azienda non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/fornitore_remove_azienda', methods=['POST'])
def fornitore_remove_azienda():
    try:
        nome = request.form['azienda-nome-fornitrice']
        material = AziendaFornitrice.query.get(nome)
        if material:
            db.session.delete(material)
            db.session.commit()
            flash('Azienda rimossa con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))

############################################## CONSULENZA ##############################################

@firm_bp.route('/consulenza_add_azienda', methods=['POST'])
def consulenza_add_azienda():
    try:
        data = request.form
        azienda = AziendaConsulenziale(
            tipologia=data['azienda-tipologia-consulenziale'],
            nome=data['azienda-nome-consulenziale'],
            note=data['azienda-note-consulenziale'],
            link=data['azienda-link-consulenziale'],
        )
        db.session.add(azienda)
        db.session.commit()
        flash('Azienda aggiunta con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante l\'aggiunta dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/consulenza_edit_azienda', methods=['POST'])
def consulenza_edit_azienda():
    try:
        data = request.form
        old_nome = AziendaConsulenziale.query.get(data['old_name_azienda_consulenziale'])
        
        if old_nome:
            old_nome.nome = data['azienda-nome-consulenziale']
            old_nome.note = data['azienda-note-consulenziale']
            old_nome.link = data['azienda-link-consulenziale']
            old_nome.tipologia = data['azienda-tipologia-consulenziale']
            db.session.commit()
            flash('Azienda modificata con successo!', 'success')
        else:
            flash('Azienda non trovata!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la modifica dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))


@firm_bp.route('/consulenza_remove_azienda', methods=['POST'])
def consulenza_remove_azienda():
    try:
        nome = request.form['azienda-nome-consulenziale']
        material = AziendaConsulenziale.query.get(nome)
        if material:
            db.session.delete(material)
            db.session.commit()
            flash('Azienda rimossa con successo!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Errore durante la rimozione dell\'azienda: {str(e)}', 'danger')
    return redirect(url_for('firms.firms'))

############################################## TEST ##############################################

# Dizionario per mappare i tipi di entità ai rispettivi modelli di SQLAlchemy
MODELLI = {
    'consulenza': MissioneConsulenza,
    'fornitore': MissioneFornitore,
    'finanziatore': MissioneFinanziatore,
}

def get_modello(tipo_entita):
    modello = MODELLI.get(tipo_entita)
    if modello is None:
        raise ValueError(f"Tipo di entità '{tipo_entita}' non supportato.")
    return modello

@firm_bp.route('/get_missioni/<tipo_entita>/<nome_entita>')
def get_missioni(tipo_entita, nome_entita):
    modello = get_modello(tipo_entita)
    missioni = modello.query.filter_by(nomeAzienda=nome_entita).all()
    missioni_data = [{'idMissione': missione.idMissione} for missione in missioni]
    return jsonify({'missioni': missioni_data})


@firm_bp.route('/manage_mission/<tipo_entita>/<nome_entita>', methods=['POST'])
def manage_mission(tipo_entita, nome_entita):
    data = request.get_json()
    action = data['action']
    missionId = data['missionId']

    modello = get_modello(tipo_entita)

    # Controlla se la missione esiste nel database
    missione_esistente = db.session.query(db.exists().where(Missione.id == missionId)).scalar()
    if not missione_esistente:
        return jsonify({'success': False, 'message': 'ID missione non esistente.'})

    if action == 'aggiungi':
        nuova_missione = modello(idMissione=missionId, nomeAzienda=nome_entita)
        db.session.add(nuova_missione)
        db.session.commit()
    elif action == 'modifica':
        missione = modello.query.filter_by(idMissione=missionId, nomeAzienda=nome_entita).first()
        if missione:
            missione.idMissione = missionId
            db.session.commit()
    elif action == 'rimuovi':
        missione = modello.query.filter_by(idMissione=missionId, nomeAzienda=nome_entita).first()
        if missione:
            db.session.delete(missione)
            db.session.commit()

    return jsonify({'success': True})
