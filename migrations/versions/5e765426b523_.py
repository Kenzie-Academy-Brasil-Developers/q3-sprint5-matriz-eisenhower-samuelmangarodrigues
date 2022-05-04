"""empty message

Revision ID: 5e765426b523
Revises: 8fe63f4b1a0e
Create Date: 2022-05-03 13:42:24.983324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e765426b523'
down_revision = '8fe63f4b1a0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eisenhowers', sa.Column('type', sa.String(length=100), nullable=True))
    op.drop_column('eisenhowers', 'eisenhowers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eisenhowers', sa.Column('eisenhowers', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('eisenhowers', 'type')
    # ### end Alembic commands ###