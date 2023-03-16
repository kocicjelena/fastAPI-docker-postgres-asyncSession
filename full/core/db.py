from sys import modules
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
#from sqlmodel.ext.asyncio.session import AsyncSession
#https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
from .config import settings
# from app import settings


from dotenv import load_dotenv
import os

load_dotenv()

db_connection_str = os.environ.get('ASYNC_CONN_STR')
async_engine = create_async_engine(
    db_connection_str,
    echo=True,
    future=True
)


async def get_async_session() -> None:
    async_session = sessionmaker(
        bind=async_engine, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
# ?
Base = declarative_base()
