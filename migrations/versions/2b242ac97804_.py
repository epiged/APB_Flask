"""empty message

Revision ID: 2b242ac97804
Revises: f4d26fbe006a
Create Date: 2024-02-05 13:47:00.970553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b242ac97804'
down_revision = 'f4d26fbe006a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prix', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produit', schema=None) as batch_op:
        batch_op.drop_column('prix')

    # ### end Alembic commands ###