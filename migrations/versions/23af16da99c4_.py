"""empty message

Revision ID: 23af16da99c4
Revises: 2e657ce3a2ac
Create Date: 2024-04-23 19:55:57.981198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23af16da99c4'
down_revision = '2e657ce3a2ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.add_column(sa.Column('borrower_name', sa.String(length=64), nullable=True))
        batch_op.drop_index('ix_borrow_borrower')
        batch_op.create_index(batch_op.f('ix_borrow_borrower_name'), ['borrower_name'], unique=False)
        batch_op.drop_column('borrower')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.add_column(sa.Column('borrower', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_index(batch_op.f('ix_borrow_borrower_name'))
        batch_op.create_index('ix_borrow_borrower', ['borrower'], unique=False)
        batch_op.drop_column('borrower_name')

    # ### end Alembic commands ###
