"""create triggerings

Revision ID: 131bc5ccb4c0
Revises: 03ec049c874e
Create Date: 2025-02-04 16:22:51.256362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '131bc5ccb4c0'
down_revision: Union[str, None] = '03ec049c874e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('customer_id_sm', sa.Integer(), nullable=True),
    sa.Column('circumstances', sa.Text(), nullable=True),
    sa.Column('violation_type', sa.String(length=255), nullable=True),
    sa.Column('fine_type', sa.String(length=255), nullable=True),
    sa.Column('request_amount', sa.Double(), nullable=True),
    sa.Column('recognition_amount', sa.Double(), nullable=True),
    sa.Column('fine_number', sa.String(length=255), nullable=True),
    sa.Column('fine_date', sa.DateTime(), nullable=True),
    sa.Column('decision', sa.String(length=255), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id_sm'], ['customers.id_sm'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    op.create_table('triggerings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('object_id_sm', sa.Integer(), nullable=True),
    sa.Column('post_id_sm', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('customer', sa.String(length=255), nullable=True),
    sa.Column('reason', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('place', sa.String(length=255), nullable=True),
    sa.Column('departure_mg', sa.SmallInteger(), nullable=True),
    sa.Column('departure_time', sa.DateTime(), nullable=True),
    sa.Column('arrival_time', sa.DateTime(), nullable=True),
    sa.Column('response_time', sa.Time(), nullable=True),
    sa.Column('mg_moment_of_actuation', sa.String(length=255), nullable=True),
    sa.Column('trigger_date', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['object_id_sm'], ['objects.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['post_id_sm'], ['posts.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('triggerings')
    op.drop_table('fines')
    # ### end Alembic commands ###
