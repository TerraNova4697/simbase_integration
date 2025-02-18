"""Changed operatings mode to str

Revision ID: ba660254e458
Revises: 9e0f48aa7d3e
Create Date: 2025-02-18 09:26:28.960290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba660254e458'
down_revision: Union[str, None] = '9e0f48aa7d3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'operating_mode',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'operating_mode',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
