"""altered column posts

Revision ID: a3d19138324b
Revises: 2f985d5fe8cf
Create Date: 2025-02-10 12:44:17.976129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3d19138324b'
down_revision: Union[str, None] = '2f985d5fe8cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'shift_mode',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'shift_mode',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
