import sys

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine
from psycopg2 import OperationalError

from icon_governance.config import settings
from icon_governance.models.preps import Prep

SQLALCHEMY_DATABASE_URL_STUB = "://{user}:{password}@{server}:{port}/{db}".format(
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    server=settings.POSTGRES_SERVER,
    port=settings.POSTGRES_PORT,
    db=settings.POSTGRES_DATABASE,
)

ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg" + SQLALCHEMY_DATABASE_URL_STUB
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2" + SQLALCHEMY_DATABASE_URL_STUB

logger.info(f"Connecting to server: {settings.POSTGRES_SERVER} and {settings.POSTGRES_DATABASE}")

async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    echo=False,
    future=True,
    pool_size=10,
    max_overflow=5,
)


# Run onetime if we want to init with a prebuilt table of attributes
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session


engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_factory = sessionmaker(bind=engine)
