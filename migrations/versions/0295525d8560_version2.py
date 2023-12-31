"""version2

Revision ID: 0295525d8560
Revises: 
Create Date: 2023-06-26 13:42:15.429965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0295525d8560'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('type_defauts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_dernier_rappel', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('type_defauts', schema=None) as batch_op:
        batch_op.drop_column('date_dernier_rappel')

    # ### end Alembic commands ###
