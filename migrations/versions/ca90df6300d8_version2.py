"""version2

Revision ID: ca90df6300d8
Revises: bc98f74a1808
Create Date: 2023-07-06 07:19:34.099346

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca90df6300d8'
down_revision = 'bc98f74a1808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.alter_column('defaut',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tickets', schema=None) as batch_op:
        batch_op.alter_column('defaut',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###
