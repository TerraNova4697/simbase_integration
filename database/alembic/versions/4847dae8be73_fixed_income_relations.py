"""Fixed income relations

Revision ID: 4847dae8be73
Revises: 719ff1ab5b49
Create Date: 2025-02-03 15:16:23.989289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4847dae8be73'
down_revision: Union[str, None] = '719ff1ab5b49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'income', 'customers', ['customer_id_sm'], ['id_sm'], ondelete='NO ACTION')
    op.create_foreign_key(None, 'income', 'objects', ['object_id_sm'], ['id_sm'], ondelete='NO ACTION')
    op.create_foreign_key(None, 'income', 'contract', ['contract_id_sm'], ['id_sm'], ondelete='NO ACTION')
    op.create_foreign_key(None, 'income', 'filials', ['filial_id_sm'], ['id_sm'], ondelete='NO ACTION')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'income', type_='foreignkey')
    op.drop_constraint(None, 'income', type_='foreignkey')
    op.drop_constraint(None, 'income', type_='foreignkey')
    op.drop_constraint(None, 'income', type_='foreignkey')
    # ### end Alembic commands ###
