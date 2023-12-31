"""ddfs

Revision ID: 708fa3ba37dc
Revises: a106c2fc11af
Create Date: 2023-07-13 15:10:02.202792

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '708fa3ba37dc'
down_revision = 'a106c2fc11af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.alter_column('evaluateur',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=40),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.alter_column('evaluateur',
               existing_type=sa.String(length=40),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=True)

    # ### end Alembic commands ###
