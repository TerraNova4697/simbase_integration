"""Updated sql error model

Revision ID: 82aac86ead2c
Revises: 8f5b5487a6ed
Create Date: 2025-01-30 14:10:47.175572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82aac86ead2c'
down_revision: Union[str, None] = '8f5b5487a6ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sql_errors', sa.Column('target_model', sa.String(length=127), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sql_errors', 'target_model')
    # ### end Alembic commands ###
