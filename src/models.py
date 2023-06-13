from sqlalchemy import Column, VARCHAR, TEXT, DECIMAL, INT, ForeignKey

from .database import Base


class Category(Base):
    name = Column(VARCHAR(64), nullable=False, unique=True, index=True)
    slug = Column(VARCHAR(64), nullable=False, unique=True, index=True)


class Product(Base):
    name = Column(VARCHAR(128), nullable=False)
    description = Column(TEXT, nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    image = Column(VARCHAR(256), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
