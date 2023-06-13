"""product data migration

Revision ID: e4be6ad95f0f
Revises: 211b8228de12
Create Date: 2023-06-13 19:25:27.408168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4be6ad95f0f'
down_revision = '211b8228de12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'product',
            sa.column('name', sa.VARCHAR(128)),
            sa.column('description', sa.TEXT),
            sa.column('price', sa.DECIMAL(8, 2)),
            sa.column('image', sa.VARCHAR(256)),
            sa.column('category_id', sa.INT)
        ),
        [
            {
                'name': 'Product1',
                'description': 'product-1',
                'price': 100,
                'image': 'shop/assets/images/product/medium-size/1-1-270x300.jpg',
                'category_id': 1
            },
            {
                'name': 'Product2',
                'description': 'product-2',
                'price': 150,
                'image': 'shop/assets/images/product/medium-size/1-1-270x300.jpg',
                'category_id': 2
            },
            {
                'name': 'Product3',
                'description': 'product-3',
                'price': 90,
                'image': 'shop/assets/images/product/medium-size/1-1-270x300.jpg',
                'category_id': 1
            }
        ]
    )


def downgrade() -> None:
    pass
