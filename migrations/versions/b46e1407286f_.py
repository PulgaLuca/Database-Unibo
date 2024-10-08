"""empty message

Revision ID: b46e1407286f
Revises: 
Create Date: 2024-08-16 11:51:31.564494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b46e1407286f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('azienda_consulenziale',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('tipologia', sa.String(length=100), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('azienda_finanziatrice',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('importo', sa.Float(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('azienda_fornitrice',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('quantita', sa.Integer(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('dipartimento',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('luogo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stato', sa.String(length=100), nullable=True),
    sa.Column('regione', sa.String(length=100), nullable=True),
    sa.Column('citta', sa.String(length=100), nullable=True),
    sa.Column('via', sa.String(length=100), nullable=True),
    sa.Column('civico', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materiale',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('membro',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('cognome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('motore',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('produttore', sa.String(length=100), nullable=True),
    sa.Column('spinta', sa.Float(), nullable=True),
    sa.Column('impulso', sa.Float(), nullable=True),
    sa.Column('massa', sa.Float(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('obiettivo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paracadute',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('modello', sa.String(length=100), nullable=True),
    sa.Column('diametro', sa.Float(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('payload',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('massa', sa.Float(), nullable=True),
    sa.Column('lunghezza', sa.Float(), nullable=True),
    sa.Column('larghezza', sa.Float(), nullable=True),
    sa.Column('altezza', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ruolo',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('sensore',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=True),
    sa.Column('unitaMisura', sa.String(length=50), nullable=True),
    sa.Column('accuratezza', sa.Float(), nullable=True),
    sa.Column('frequenza', sa.Float(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('razzo',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('massa', sa.Float(), nullable=True),
    sa.Column('lunghezza', sa.Float(), nullable=True),
    sa.Column('larghezza', sa.Float(), nullable=True),
    sa.Column('altezza', sa.Float(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('nomeMotore', sa.String(length=50), nullable=False),
    sa.Column('nomeParacadute', sa.String(length=50), nullable=False),
    sa.Column('nomeMateriale', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['nomeMateriale'], ['materiale.nome'], ),
    sa.ForeignKeyConstraint(['nomeMotore'], ['motore.nome'], ),
    sa.ForeignKeyConstraint(['nomeParacadute'], ['paracadute.nome'], ),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('team',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('nomeDipartimento', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['nomeDipartimento'], ['dipartimento.nome'], ),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('incarico',
    sa.Column('dataInizio', sa.Date(), nullable=False),
    sa.Column('dataFine', sa.Date(), nullable=True),
    sa.Column('nomeTeam', sa.String(length=100), nullable=False),
    sa.Column('idMembro', sa.Integer(), nullable=False),
    sa.Column('nomeRuolo', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idMembro'], ['membro.id'], ),
    sa.ForeignKeyConstraint(['nomeRuolo'], ['ruolo.nome'], ),
    sa.ForeignKeyConstraint(['nomeTeam'], ['team.nome'], ),
    sa.PrimaryKeyConstraint('dataInizio', 'nomeTeam', 'idMembro', 'nomeRuolo')
    )
    op.create_table('missione',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('dataLancio', sa.Date(), nullable=True),
    sa.Column('stato', sa.String(length=100), nullable=True),
    sa.Column('idLuogo', sa.Integer(), nullable=False),
    sa.Column('idPayload', sa.Integer(), nullable=False),
    sa.Column('nomeRazzo', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idLuogo'], ['luogo.id'], ),
    sa.ForeignKeyConstraint(['idPayload'], ['payload.id'], ),
    sa.ForeignKeyConstraint(['nomeRazzo'], ['razzo.nome'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('razzo_sensore',
    sa.Column('nomeRazzo', sa.String(length=100), nullable=False),
    sa.Column('nomeSensore', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['nomeRazzo'], ['razzo.nome'], ),
    sa.ForeignKeyConstraint(['nomeSensore'], ['sensore.nome'], ),
    sa.PrimaryKeyConstraint('nomeRazzo', 'nomeSensore')
    )
    op.create_table('simulazione',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('nomeTeam', sa.String(length=100), nullable=False),
    sa.Column('nomeRazzo', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['nomeRazzo'], ['razzo.nome'], ),
    sa.ForeignKeyConstraint(['nomeTeam'], ['team.nome'], ),
    sa.PrimaryKeyConstraint('id', 'nomeRazzo')
    )
    op.create_table('dato_sensore',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('valore', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('idMissione', sa.Integer(), nullable=False),
    sa.Column('nomeSensore', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idMissione'], ['missione.id'], ),
    sa.ForeignKeyConstraint(['nomeSensore'], ['sensore.nome'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('missione_consulenza',
    sa.Column('idMissione', sa.Integer(), nullable=False),
    sa.Column('nomeAzienda', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idMissione'], ['missione.id'], ),
    sa.ForeignKeyConstraint(['nomeAzienda'], ['azienda_consulenziale.nome'], ),
    sa.PrimaryKeyConstraint('idMissione', 'nomeAzienda')
    )
    op.create_table('missione_finanziatore',
    sa.Column('idMissione', sa.Integer(), nullable=False),
    sa.Column('nomeAzienda', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idMissione'], ['missione.id'], ),
    sa.ForeignKeyConstraint(['nomeAzienda'], ['azienda_finanziatrice.nome'], ),
    sa.PrimaryKeyConstraint('idMissione', 'nomeAzienda')
    )
    op.create_table('missione_fornitore',
    sa.Column('idMissione', sa.Integer(), nullable=False),
    sa.Column('nomeAzienda', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['idMissione'], ['missione.id'], ),
    sa.ForeignKeyConstraint(['nomeAzienda'], ['azienda_fornitrice.nome'], ),
    sa.PrimaryKeyConstraint('idMissione', 'nomeAzienda')
    )
    op.create_table('missione_obiettivo',
    sa.Column('idMissione', sa.Integer(), nullable=False),
    sa.Column('idObiettivo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idMissione'], ['missione.id'], ),
    sa.ForeignKeyConstraint(['idObiettivo'], ['obiettivo.id'], ),
    sa.PrimaryKeyConstraint('idMissione', 'idObiettivo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('missione_obiettivo')
    op.drop_table('missione_fornitore')
    op.drop_table('missione_finanziatore')
    op.drop_table('missione_consulenza')
    op.drop_table('dato_sensore')
    op.drop_table('simulazione')
    op.drop_table('razzo_sensore')
    op.drop_table('missione')
    op.drop_table('incarico')
    op.drop_table('team')
    op.drop_table('razzo')
    op.drop_table('sensore')
    op.drop_table('ruolo')
    op.drop_table('payload')
    op.drop_table('paracadute')
    op.drop_table('obiettivo')
    op.drop_table('motore')
    op.drop_table('membro')
    op.drop_table('materiale')
    op.drop_table('luogo')
    op.drop_table('dipartimento')
    op.drop_table('azienda_fornitrice')
    op.drop_table('azienda_finanziatrice')
    op.drop_table('azienda_consulenziale')
    # ### end Alembic commands ###
