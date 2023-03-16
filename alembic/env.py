import asyncio
import logging
from logging.config import fileConfig
import os
from json import loads
from core.orm.models import Base
from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine

config = context.config
logger = logging.getLogger(__name__)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
con_url = os.getenv("ASYNC_CONN_STR")
config.set_main_option("sqlalchemy.url", con_url)
target_metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)"
          "s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

from app.heroes.models import Hero  # noqa: 'autogenerate' support

exclude_tables = loads(os.getenv("DB_EXCLUDE_TABLES"))


def filter_db_objects(
        object,  # noqa: indirect usage
        name,
        type_,
        *args,  # noqa: indirect usage
        **kwargs  # noqa: indirect usage
):
    if type_ == "table":
        return name not in exclude_tables

    if type_ == "index" and name.startswith("idx") and name.endswith("geom"):
        return False

    return True


def run_migrations_offline():
    #url = os.getenv("ASYNC_CONN_STR")
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
       # dialect_opts={"paramstyle": "named"},
       # include_object=filter_db_objects
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            #include_object=filter_db_objects
        )
        context.run_migrations()


async def run_migrations_online():
    config_section = config.get_section(config.config_ini_section)
    #url = os.getenv("ASYNC_CONN_STR")
    url = config.get_main_option("sqlalchemy.url")
    config_section["sqlalchemy.url"] = url

    connectable = AsyncEngine(
        engine_from_config(
            config_section,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    logger.warn("--- Running migrations offline ---")
    run_migrations_offline()
else:
    logger.warn("Running migrations online")
    asyncio.run(run_migrations_online())
