"""empty message

Revision ID: 73bf02535680
Revises: 8279b2042409
Create Date: 2022-05-16 13:14:01.378581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73bf02535680'
down_revision = '8279b2042409'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo__question', schema=None) as batch_op:
        batch_op.drop_column('memo_subject')
        batch_op.drop_column('memo_create_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo__question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('memo_create_date', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('memo_subject', sa.VARCHAR(length=200), nullable=False))

    # ### end Alembic commands ###
