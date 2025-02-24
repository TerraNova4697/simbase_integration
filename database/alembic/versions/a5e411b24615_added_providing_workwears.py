"""Added providing_workwears

Revision ID: a5e411b24615
Revises: b4713c1663a6
Create Date: 2025-02-24 12:26:45.919636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5e411b24615'
down_revision: Union[str, None] = 'b4713c1663a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('providing_workwears', sa.Column('sm_state', sa.String(length=255), nullable=True))
    op.drop_constraint('providing_workwears_id_sm_key', 'providing_workwears', type_='unique')
    op.drop_column('providing_workwears', 'id_sm')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('providing_workwears', sa.Column('id_sm', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_unique_constraint('providing_workwears_id_sm_key', 'providing_workwears', ['id_sm'])
    op.drop_column('providing_workwears', 'sm_state')
    # ### end Alembic commands ###
