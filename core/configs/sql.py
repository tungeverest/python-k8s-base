from os import getenv
from typing import Optional

from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    DB_RETRIES: int = getenv("DB_RETRIES", 5)
    DB_RETRIES_DELAY: int = getenv("DB_RETRIES_DELAY", 1)
    DB_RETRIES_BACKOFF: int = getenv("DB_RETRIES_BACKOFF", 2)
    DB_ECHO: bool = getenv("DB_ECHO", False)

    SQL_DB: str = getenv("POSTGRES_DB", "test")
    SQL_HOST: str = getenv("SQL_HOST", "postgresdb-svc")
    SQL_PORT: int = int(getenv("SQL_PORT", "5432"))
    SQL_USER: str = getenv("POSTGRES_USER", "")
    SQL_PASSWORD: str = getenv("POSTGRES_PASSWORD", "")

    SQLALCHEMY_POOL_SIZE: int = getenv("SQLALCHEMY_POOL_SIZE", 5)
    SQLALCHEMY_MAX_OVERFLOW: int = getenv("SQLALCHEMY_MAX_OVERFLOW", 5)
    SQLALCHEMY_POOL_TIMEOUT: int = getenv("SQLALCHEMY_POOL_TIMEOUT", 60)
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    SQLALCHEMY_DATABASE_URL: Optional[str] = f"postgresql+psycopg2://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}" #noqa
    print("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
