"""user_security_totp

Revision ID: 34abe1407b85
Revises: 
Create Date: 2026-04-23 16:43:21.315776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34abe1407b85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_security_totp',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.UnicodeText(), nullable=False),
        sa.Column('secret', sa.UnicodeText(), nullable=False),
        sa.Column('last_successful_challenge', sa.DateTime(), nullable=True),
    )


def downgrade():
    pass
