"""Changed field type

Revision ID: 6da32d296632
Revises: 4847dae8be73
Create Date: 2025-02-03 16:19:32.624606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6da32d296632'
down_revision: Union[str, None] = '4847dae8be73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income', 'comment',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income', 'comment',
               existing_type=sa.String(length=255),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    # ### end Alembic commands ###
