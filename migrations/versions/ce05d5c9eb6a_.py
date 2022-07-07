"""empty message

Revision ID: ce05d5c9eb6a
Revises: 
Create Date: 2022-07-06 18:40:44.998037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce05d5c9eb6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dono',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.String(length=2), nullable=True),
    sa.Column('data_nascimento', sa.String(length=10), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('endereco', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('insumos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('codigo', sa.String(length=2), nullable=True),
    sa.Column('data_validade', sa.String(length=10), nullable=True),
    sa.Column('preco', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.String(length=3), nullable=True),
    sa.Column('data_nascimento', sa.String(length=10), nullable=True),
    sa.Column('endereco', sa.String(length=100), nullable=True),
    sa.Column('cpf', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=10), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('data_consulta', sa.String(length=11), nullable=True),
    sa.Column('marcela_dono', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['marcela_dono'], ['dono.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    op.create_table('insumos_funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('funcionarios', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['funcionarios'], ['funcionario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('insumos_funcionario')
    op.drop_table('cliente')
    op.drop_table('insumos')
    op.drop_table('funcionario')
    op.drop_table('dono')
    # ### end Alembic commands ###
