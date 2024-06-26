"""update text length in  panel 

Revision ID: 9275a0ceeff4
Revises: 19bbaac7c13a
Create Date: 2024-04-29 22:49:44.275214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9275a0ceeff4'
down_revision: Union[str, None] = '19bbaac7c13a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pv_panel', 'cell_technology',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'dimensions',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'weight',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'product_warranty',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'power_output_warranty',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'open_circuit_voltage',
               existing_type=sa.NUMERIC(precision=4, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'short_circuit_current',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'max_power_voltage',
               existing_type=sa.NUMERIC(precision=4, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'max_power_current',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'module_efficiency',
               existing_type=sa.NUMERIC(precision=4, scale=1),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'power_temp_coeff',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'voltage_temp_coeff',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'current_temp_coeff',
               existing_type=sa.NUMERIC(precision=5, scale=3),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'operating_temp_range',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'junction_box',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('pv_panel', 'connector',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pv_panel', 'connector',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('pv_panel', 'junction_box',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('pv_panel', 'operating_temp_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('pv_panel', 'current_temp_coeff',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=5, scale=3),
               existing_nullable=True)
    op.alter_column('pv_panel', 'voltage_temp_coeff',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'power_temp_coeff',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'module_efficiency',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=4, scale=1),
               existing_nullable=True)
    op.alter_column('pv_panel', 'max_power_current',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'max_power_voltage',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=4, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'short_circuit_current',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'open_circuit_voltage',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=4, scale=2),
               existing_nullable=True)
    op.alter_column('pv_panel', 'power_output_warranty',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('pv_panel', 'product_warranty',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('pv_panel', 'weight',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('pv_panel', 'dimensions',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('pv_panel', 'cell_technology',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    # ### end Alembic commands ###
