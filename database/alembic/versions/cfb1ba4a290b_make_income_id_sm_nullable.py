"""Make income.id_sm nullable

Revision ID: cfb1ba4a290b
Revises: 3fbca64d8a92
Create Date: 2025-02-05 08:57:37.187894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfb1ba4a290b'
down_revision: Union[str, None] = '3fbca64d8a92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income', 'id_sm',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income', 'id_sm',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
