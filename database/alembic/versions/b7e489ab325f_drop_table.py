"""drop table

Revision ID: b7e489ab325f
Revises: c187f40f3c3b
Create Date: 2025-02-17 12:30:26.846182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b7e489ab325f'
down_revision: Union[str, None] = 'c187f40f3c3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contract_TRU')
    # op.drop_constraint('legal_claims_contract_TRU_id_sm_fkey', 'legal_claims', type_='foreignkey')
    op.drop_column('legal_claims', 'contract_TRU_id_sm')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('legal_claims', sa.Column('contract_TRU_id_sm', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('legal_claims_contract_TRU_id_sm_fkey', 'legal_claims', 'contract_TRU', ['contract_TRU_id_sm'], ['id_sm'])
    op.create_table('contract_TRU',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_sm', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('date_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('sm_state', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contract_TRU_pkey'),
    sa.UniqueConstraint('id_sm', name='contract_TRU_id_sm_key')
    )
    # ### end Alembic commands ###
