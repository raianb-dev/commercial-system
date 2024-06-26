"""empty message

Revision ID: 60fc6fbb4126
Revises: 74bdbbe284b0
Create Date: 2024-04-15 16:57:22.619820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60fc6fbb4126'
down_revision: Union[str, None] = '74bdbbe284b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('status', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Orders', 'status')
    # ### end Alembic commands ###
