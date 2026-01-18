"""add series episode metadata

Revision ID: 7b8a4d3c2f1a
Revises: 50d63e3650d2
Create Date: 2026-01-18

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b8a4d3c2f1a'
down_revision = '50d63e3650d2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('job', sa.Column('season_number', sa.Integer(), nullable=True))
    op.add_column('track', sa.Column('episode_number', sa.Integer(), nullable=True))
    op.add_column('track', sa.Column('episode_title', sa.String(length=256), nullable=True))


def downgrade():
    op.drop_column('track', 'episode_title')
    op.drop_column('track', 'episode_number')
    op.drop_column('job', 'season_number')
