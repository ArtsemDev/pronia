from typing import List

from fastapi import Query
from sqlalchemy import select

from .router import router
from ..models import Product
from ..schemas import ProductSchema, ContactForm


@router.get('/product', response_model=List[ProductSchema])
async def product(category_id: int = Query(default=0), q: str = Query(default='')):
    async with Product.session() as session:
        sql = select(Product).filter(Product.name.contains(q)).order_by(Product.name).limit(15)
        if category_id:
            sql = sql.filter_by(category_id=category_id)
        products = await session.scalars(sql)
        return [ProductSchema.from_orm(product) for product in products]


@router.post('/contact')
async def contact(form: ContactForm):
    print(form)
    return {'status': 'ok'}
