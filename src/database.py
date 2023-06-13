from sqlalchemy import Column, INT
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.settings import SETTINGS


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    _engine = create_async_engine(SETTINGS.DATABASE_URL.build(
        scheme='postgresql+asyncpg',
        user=SETTINGS.DATABASE_URL.user,
        password=SETTINGS.DATABASE_URL.password,
        host=SETTINGS.DATABASE_URL.host,
        port=SETTINGS.DATABASE_URL.port,
        query=SETTINGS.DATABASE_URL.query,
        path=SETTINGS.DATABASE_URL.path,
        fragment=SETTINGS.DATABASE_URL.fragment
    ))
    session = async_sessionmaker(bind=_engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')
