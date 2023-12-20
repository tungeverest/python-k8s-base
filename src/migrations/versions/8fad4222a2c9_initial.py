"""initial

Revision ID: 8fad4222a2c9
Revises: 
Create Date: 2023-11-22 05:04:21.338115

"""
import sqlmodel
from alembic import op
import sqlalchemy as sa
# import sqlalchemy_utils
import sqlmodel.sql.sqltypes
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = '8fad4222a2c9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('nickname', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('current_timestamp(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('current_timestamp(0)'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), server_default=sa.text('current_timestamp(0)'), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_heroes_id'), ['id'], unique=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_heroes_id'))

    op.drop_table('heroes')
    # ### end Alembic commands ###
