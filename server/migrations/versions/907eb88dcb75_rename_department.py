"""rename department

Revision ID: 907eb88dcb75
Revises: 9fbf490bb86f
Create Date: 2024-03-06 10:04:47.500082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907eb88dcb75'
down_revision = '9fbf490bb86f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
