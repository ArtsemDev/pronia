"""category data migration

Revision ID: 211b8228de12
Revises: 1f4c91d71175
Create Date: 2023-06-13 19:23:39.569122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211b8228de12'
down_revision = '1f4c91d71175'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'category',
            sa.column('name', sa.VARCHAR(64)),
            sa.column('slug', sa.VARCHAR(64)),
        ),
        [
            {'name': 'Bansai', 'slug': 'bansai'},
            {'name': 'House Plants', 'slug': 'house-plants'},
        ]
    )


def downgrade() -> None:
    pass
