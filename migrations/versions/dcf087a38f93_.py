"""empty message

Revision ID: dcf087a38f93
Revises: fa1b4c72ffed
Create Date: 2021-03-24 23:23:43.647740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcf087a38f93'
down_revision = 'fa1b4c72ffed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('slug', table_name='posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('slug', 'posts', ['slug'], unique=True)
    # ### end Alembic commands ###