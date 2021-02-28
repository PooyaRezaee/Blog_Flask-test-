"""empty message

Revision ID: be3d3ff78d1b
Revises: d389d79278cd
Create Date: 2021-02-25 23:50:55.784548

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be3d3ff78d1b'
down_revision = 'd389d79278cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=128), nullable=False),
    sa.Column('Age', sa.Integer(), nullable=False),
    sa.Column('Email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=1280), nullable=False),
    sa.Column('rol', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email')
    )
    op.drop_index('Email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('full_name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('Age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('Email', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=1280), nullable=False),
    sa.Column('rol', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('Email', 'user', ['Email'], unique=True)
    op.drop_table('users')
    # ### end Alembic commands ###
