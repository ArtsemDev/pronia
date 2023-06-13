from pydantic import EmailStr, Field
from pydantic.types import Decimal

from .types import Schema


class ProductSchema(Schema):
    name: str
    description: str
    price: Decimal
    image: str
    category_id: int


class ContactForm(Schema):
    name: str = Field(..., max_length=64)
    email: EmailStr = Field(...)
    message: str = Field(...)
