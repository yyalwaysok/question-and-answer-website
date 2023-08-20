"""empty message

Revision ID: 633c6db3a7cb
Revises: 4b49917661cd
Create Date: 2023-08-20 22:06:16.786389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '633c6db3a7cb'
down_revision = '4b49917661cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('captcha', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_captcha')
    # ### end Alembic commands ###
