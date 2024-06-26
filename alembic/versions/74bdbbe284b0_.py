"""empty message

Revision ID: 74bdbbe284b0
Revises: cf6ff213c307
Create Date: 2024-04-03 11:09:02.346476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74bdbbe284b0'
down_revision: Union[str, None] = 'cf6ff213c307'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('block', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Orders', 'block')
    # ### end Alembic commands ###
