"""create providing_workwears

Revision ID: e0ef6b6ec061
Revises: b1298564b933
Create Date: 2025-02-04 17:08:27.192377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0ef6b6ec061'
down_revision: Union[str, None] = 'b1298564b933'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('customer_id_sm', sa.Integer(), nullable=True),
    sa.Column('post_id_sm', sa.Integer(), nullable=True),
    sa.Column('log_of_accept_and_transf_of_weapon_and_ammunition', sa.Boolean(), nullable=True),
    sa.Column('finery_journal', sa.Boolean(), nullable=True),
    sa.Column('log_of_inc_info_and_recor_of_activation_of_tech_sec_means', sa.Boolean(), nullable=True),
    sa.Column('import_export_log_and_contrib_removals_of_inventory_items', sa.Boolean(), nullable=True),
    sa.Column('acceptance_log_for_premises_delivery', sa.Boolean(), nullable=True),
    sa.Column('visitor_log', sa.Boolean(), nullable=True),
    sa.Column('vehicle_registration_log', sa.Boolean(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id_sm'], ['customers.id_sm'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['post_id_sm'], ['posts.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    op.create_table('providing_workwears',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('customer_id_sm', sa.Integer(), nullable=True),
    sa.Column('post_id_sm', sa.Integer(), nullable=True),
    sa.Column('summer_set', sa.SmallInteger(), nullable=True),
    sa.Column('winter_set', sa.SmallInteger(), nullable=True),
    sa.Column('reflective_vets', sa.SmallInteger(), nullable=True),
    sa.Column('summer_shoes', sa.SmallInteger(), nullable=True),
    sa.Column('winter_shoes', sa.SmallInteger(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id_sm'], ['customers.id_sm'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['post_id_sm'], ['posts.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    op.create_table('training_and_medical_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('customer_id_sm', sa.Integer(), nullable=True),
    sa.Column('post_id_sm', sa.Integer(), nullable=True),
    sa.Column('annual_retraining_of_security_guards_quant', sa.SmallInteger(), nullable=True),
    sa.Column('anti_terrorism_training_quant', sa.SmallInteger(), nullable=True),
    sa.Column('fire_technical_minimum_quant', sa.SmallInteger(), nullable=True),
    sa.Column('annual_medical_examination_quant', sa.SmallInteger(), nullable=True),
    sa.Column('pre_shift_medical_examination_quant', sa.SmallInteger(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id_sm'], ['customers.id_sm'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['post_id_sm'], ['posts.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    op.create_table('transports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sm', sa.Integer(), nullable=False),
    sa.Column('filial_id_sm', sa.Integer(), nullable=True),
    sa.Column('customer_id_sm', sa.Integer(), nullable=True),
    sa.Column('post_id_sm', sa.Integer(), nullable=True),
    sa.Column('transport_quant', sa.SmallInteger(), nullable=True),
    sa.Column('additional_necessary_transport_quant', sa.SmallInteger(), nullable=True),
    sa.Column('GPS', sa.SmallInteger(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id_sm'], ['customers.id_sm'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filial_id_sm'], ['filials.id_sm'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['post_id_sm'], ['posts.id_sm'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_sm')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transports')
    op.drop_table('training_and_medical_services')
    op.drop_table('providing_workwears')
    op.drop_table('journals')
    # ### end Alembic commands ###
