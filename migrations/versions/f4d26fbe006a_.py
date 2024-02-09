"""empty message

Revision ID: f4d26fbe006a
Revises: 
Create Date: 2024-02-05 08:12:53.434071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d26fbe006a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nom')
    )
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.Column('prenom', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('mot_pass', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=50), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_email', sa.String(length=50), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email')
    )
    op.create_table('produit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(length=50), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('categorie', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categorie'], ['categorie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produit')
    op.drop_table('contact')
    op.drop_table('utilisateur')
    op.drop_table('categorie')
    # ### end Alembic commands ###
