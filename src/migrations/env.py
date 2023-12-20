import os
import asyncio

from alembic import context
from sqlalchemy import pool
from sqlmodel import SQLModel
from asyncpg import Connection
# from logging.config import fileConfig
from sqlalchemy.ext.asyncio import async_engine_from_config
from src import models

config = context.config
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
target_metadata = SQLModel.metadata
target_metadata.naming_convention = NAMING_CONVENTION


def run_migrations_offline() -> None:
    context.configure(
        url=os.environ["SQLALCHEMY_DATABASE_URL"],
        literal_binds=True,
        target_metadata=target_metadata,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,
        user_module_prefix="sqlmodel.sql.sqltypes.",
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section)
    connectable = async_engine_from_config(
        configuration,
        url=os.environ["SQLALCHEMY_DATABASE_URL"],
        future=True,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
