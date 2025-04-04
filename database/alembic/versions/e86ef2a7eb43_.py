"""empty message

Revision ID: e86ef2a7eb43
Revises: 27d6aedd43f1
Create Date: 2025-02-05 11:19:07.801182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e86ef2a7eb43'
down_revision: Union[str, None] = '27d6aedd43f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shifts', sa.Column('security_guard_replaced_id_sm', sa.Integer(), nullable=True))
    op.drop_constraint('shifts_security_guard_replaces_id_sm_fkey', 'shifts', type_='foreignkey')
    op.create_foreign_key(None, 'shifts', 'security_guards', ['security_guard_replaced_id_sm'], ['id_sm'], ondelete='NO ACTION')
    op.drop_column('shifts', 'security_guard_replaces_id_sm')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shifts', sa.Column('security_guard_replaces_id_sm', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shifts', type_='foreignkey')
    op.create_foreign_key('shifts_security_guard_replaces_id_sm_fkey', 'shifts', 'security_guards', ['security_guard_replaces_id_sm'], ['id_sm'])
    op.drop_column('shifts', 'security_guard_replaced_id_sm')
    # ### end Alembic commands ###
