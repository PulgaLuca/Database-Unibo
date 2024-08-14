from .extensions import db

# Classe per la tabella 'Membro'
class Membro(db.Model):
    __tablename__ = "membro"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cognome = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))
    incarichi = db.relationship('incarico', backref='membro', lazy=True)

# Classe per la tabella 'Ruolo'
class Ruolo(db.Model):
    __tablename__ = "ruolo"

    nome = db.Column(db.String(100), primary_key=True)
    incarichi = db.relationship('incarico', backref='ruolo', lazy=True)

# Classe per la tabella 'Dipartimento'
class Dipartimento(db.Model):
    __tablename__ = "dipartimento"

    nome = db.Column(db.String(100), primary_key=True)
    teams = db.relationship('team', backref='dipartimento', lazy=True)

# Classe per la tabella 'Team'
class Team(db.Model):
    __tablename__ = "team"

    nome = db.Column(db.String(100), primary_key=True)
    nomeDipartimento = db.Column(db.String(100), db.ForeignKey('dipartimento.nome'), nullable=False)
    incarichi = db.relationship('Incarico', backref='team', lazy=True)
    simulazioni = db.relationship('simulazione', backref='team', lazy=True)

# Classe per la tabella 'Incarico'
class Incarico(db.Model):
    __tablename__ = "incarico"

    dataInizio = db.Column(db.Date, primary_key=True)
    dataFine = db.Column(db.Date, nullable=True)
    nomeTeam = db.Column(db.String(100), db.ForeignKey('team.nome'), primary_key=True, nullable=False)
    idMembro = db.Column(db.Integer, db.ForeignKey('membro.id'), primary_key=True, nullable=False)
    nomeRuolo = db.Column(db.String(100), db.ForeignKey('ruolo.nome'), primary_key=True, nullable=False)

# Classe per la tabella 'Luogo'
class Luogo(db.Model):
    __tablename__ = "luogo"
    
    id = db.Column(db.Integer, primary_key=True)
    stato = db.Column(db.String(100))
    regione = db.Column(db.String(100))
    citta = db.Column(db.String(100))
    via = db.Column(db.String(100))
    civico = db.Column(db.String(10))
    missioni = db.relationship('missione', backref='luogo', lazy=True)

# Classe per la tabella 'Obiettivo'
class Obiettivo(db.Model):
    __tablename__ = "obiettivo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    missioni_obiettivo = db.relationship('missione_obiettivo', backref='obiettivo', lazy=True)

# Classe per la tabella 'Payload'
class Payload(db.Model):
    __tablename__ = "payload"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    massa = db.Column(db.Float)
    lunghezza = db.Column(db.Float)
    larghezza = db.Column(db.Float)
    altezza = db.Column(db.Float)
    missioni = db.relationship('missione', backref='payload', lazy=True)

# Classe per la tabella 'Materiale'
class Materiale(db.Model):
    __tablename__ = "materiale"

    nome = db.Column(db.String(100), primary_key=True)
    note = db.Column(db.Text)
    razzi = db.relationship('razzo', backref='materiale', lazy=True)

# Classe per la tabella 'Motore'
class Motore(db.Model):
    __tablename__ = "motore"

    nome = db.Column(db.String(100), primary_key=True)
    produttore = db.Column(db.String(100))
    spinta = db.Column(db.Float)
    impulso = db.Column(db.Float)
    massa = db.Column(db.Float)
    link = db.Column(db.Text, nullable=True)
    razzi = db.relationship('razzo', backref='motore', lazy=True)

# Classe per la tabella 'Paracadute'
class Paracadute(db.Model):
    __tablename__ = "paracadute"

    nome = db.Column(db.String(100), primary_key=True)
    modello = db.Column(db.String(100))
    diametro = db.Column(db.Float)
    link = db.Column(db.Text, nullable=True)
    razzi = db.relationship('razzo', backref='paracadute', lazy=True)

# Classe per la tabella 'Razzo'
class Razzo(db.Model):
    __tablename__ = "razzo"

    nome = db.Column(db.String(100), primary_key=True)
    massa = db.Column(db.Float)
    lunghezza = db.Column(db.Float)
    larghezza = db.Column(db.Float)
    altezza = db.Column(db.Float)
    link = db.Column(db.Text, nullable=True)
    nomeMotore = db.Column(db.String(50), db.ForeignKey('motore.nome'), nullable=False)
    nomeParacadute = db.Column(db.String(50), db.ForeignKey('paracadute.nome'), nullable=False)
    nomeMateriale = db.Column(db.String(100), db.ForeignKey('materiale.nome'), nullable=False)
    missioni = db.relationship('missione', backref='razzo', lazy=True)
    razzo_sensori = db.relationship('razzo_sensore', backref='razzo', lazy=True)

    motore = db.relationship('motore', backref=db.backref('razzi', lazy=True))
    paracadute = db.relationship('paracadute', backref=db.backref('razzi', lazy=True))
    materiale = db.relationship('materiale', backref=db.backref('razzi', lazy=True))

# Classe per la tabella 'Missione'
class Missione(db.Model):
    __tablename__ = "missione"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    dataLancio = db.Column(db.Date)
    stato = db.Column(db.String(100))
    idLuogo = db.Column(db.Integer, db.ForeignKey('luogo.id'), nullable=False)
    idPayload = db.Column(db.Integer, db.ForeignKey('payload.id'), nullable=False)
    nomeRazzo = db.Column(db.String(100), db.ForeignKey('razzo.nome'), nullable=False)

    missioni_obiettivo = db.relationship('missione_obiettivo', backref='missione', lazy=True)
    missioni_fornitori = db.relationship('missione_fornitore', backref='missione', lazy=True)
    missioni_consulenza = db.relationship('missione_consulenza', backref='missione', lazy=True)
    missioni_finanziatore = db.relationship('missione_finanziatore', backref='missione', lazy=True)

# Classe per la tabella 'MissioneObiettivo'
class MissioneObiettivo(db.Model):
    __tablename__ = "missione_obiettivo"

    idMissione = db.Column(db.Integer, db.ForeignKey('missione.id'), primary_key=True)
    idObiettivo = db.Column(db.Integer, db.ForeignKey('obiettivo.id'), primary_key=True)

# Classe per la tabella 'AziendaFornitrice'
class AziendaFornitrice(db.Model):
    __tablename__ = "azienda_fornitrice"

    nome = db.Column(db.String(100), primary_key=True)
    quantita = db.Column(db.Integer)
    note = db.Column(db.Text)
    link = db.Column(db.Text, nullable=True)
    missioni_fornitori = db.relationship('missione_fornitore', backref='azienda_fornitrice', lazy=True)

# Classe per la tabella 'MissioneFornitore'
class MissioneFornitore(db.Model):
    __tablename__ = "missione_fornitore"

    idMissione = db.Column(db.Integer, db.ForeignKey('missione.id'), primary_key=True)
    nomeAzienda = db.Column(db.String(100), db.ForeignKey('azienda_fornitrice.nome'), primary_key=True)

# Classe per la tabella 'AziendaConsulenziale'
class AziendaConsulenziale(db.Model):
    __tablename__ = "azienda_consulenziale"

    nome = db.Column(db.String(100), primary_key=True)
    tipologia = db.Column(db.String(100))
    note = db.Column(db.Text)
    link = db.Column(db.Text, nullable=True)
    missioni_consulenza = db.relationship('missione_consulenza', backref='azienda_consulenziale', lazy=True)

# Classe per la tabella 'MissioneConsulenza'
class MissioneConsulenza(db.Model):
    __tablename__ = "missione_consulenza"

    idMissione = db.Column(db.Integer, db.ForeignKey('missione.id'), primary_key=True)
    nomeAzienda = db.Column(db.String(100), db.ForeignKey('azienda_consulenziale.nome'), primary_key=True)

# Classe per la tabella 'AziendaFinanziatrice'
class AziendaFinanziatrice(db.Model):
    __tablename__ = "azienda_finanziatrice"

    nome = db.Column(db.String(100), primary_key=True)
    importo = db.Column(db.Float)
    note = db.Column(db.Text)
    link = db.Column(db.Text, nullable=True)
    missioni_finanziatore = db.relationship('missione_finanziatore', backref='azienda_finanziatrice', lazy=True)

# Classe per la tabella 'MissioneFinanziatore'
class MissioneFinanziatore(db.Model):
    __tablename__ = "missione_finanziatore"

    idMissione = db.Column(db.Integer, db.ForeignKey('missione.id'), primary_key=True)
    nomeAzienda = db.Column(db.String(100), db.ForeignKey('azienda_finanziatrice.nome'), primary_key=True)

# Classe per la tabella 'Sensore'
class Sensore(db.Model):
    __tablename__ = "sensore"

    nome = db.Column(db.String(100), primary_key=True)
    tipo = db.Column(db.String(100))
    unitaMisura = db.Column(db.String(50))
    accuratezza = db.Column(db.Float)
    frequenza = db.Column(db.Float)
    link = db.Column(db.Text, nullable=True)
    dati_sensore = db.relationship('dato_sensore', backref='sensore', lazy=True)
    razzo_sensori = db.relationship('razzo_sensore', backref='sensore', lazy=True)

# Classe per la tabella 'DatoSensore'
class DatoSensore(db.Model):
    __tablename__ = "dato_sensore"

    id = db.Column(db.Integer, primary_key=True)
    valore = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    idMissione = db.Column(db.Integer, db.ForeignKey('missione.id'), nullable=False)
    nomeSensore = db.Column(db.String(100), db.ForeignKey('sensore.nome'), nullable=False)

# Classe per la tabella 'RazzoSensore'
class RazzoSensore(db.Model):
    __tablename__ = "razzo_sensore"

    nomeRazzo = db.Column(db.String(100), db.ForeignKey('razzo.nome'), primary_key=True)
    nomeSensore = db.Column(db.String(100), db.ForeignKey('sensore.nome'), primary_key=True)

# Classe per la tabella 'Simulazione'
class Simulazione(db.Model):
    __tablename__ = "simulazione"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    link = db.Column(db.Text, nullable=True)
    nomeTeam = db.Column(db.String(100), db.ForeignKey('team.nome'), nullable=False)
    nomeRazzo = db.Column(db.String(100), db.ForeignKey('razzo.nome'), primary_key=True)
