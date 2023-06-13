from sqlalchemy import select
from starlette.requests import Request

from .router import router
from ..settings import templating
from ..models import Category, Product


@router.get('/shop', name='shop_index')
async def index(request: Request):
    async with Category.session() as session:
        categories = await session.scalars(
            select(Category).order_by('id')
        )
        min_price = await session.scalar(
            select(Product.price)
            .order_by(Product.price)
            .limit(1)
        )
        max_price = await session.scalar(
            select(Product.price)
            .order_by(Product.price.desc())
            .limit(1)
        )
    return templating.TemplateResponse(
        name='shop/shop.html',
        context={
            'request': request,
            'categories': categories,
            'min_price': min_price,
            'max_price': max_price
        }
    )


@router.get('/contact', name='shop_contact')
async def contact(request: Request):
    return templating.TemplateResponse(
        name='shop/contact.html',
        context={
            'request': request
        }
    )