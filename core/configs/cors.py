from os import getenv
from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator


class CorsConfig(BaseSettings):
    # TODO: Can used Cors from database.
    MAX_AGE_CACHE: int = 3600
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    TRUSTED_HOST: List[str] = ["localhost"]
    CORS_ORIGINS_AUT: List[AnyHttpUrl] = ["https://aut.url"]
    CORS_ORIGINS_LOCAL: List[AnyHttpUrl] = [
        "http://localhost:8080",
        "http://localhost:8085"
    ]
    CORS_ORIGINS_STAGING: List[AnyHttpUrl] = ["https://stagging.url"]
    CORS_ORIGINS_PRODUCTION: List[AnyHttpUrl] = ["https://production.url"]
    CORS_ORIGINS_DEVELOPMENT: List[AnyHttpUrl] = ["http://development.url"]
    CORS_ORIGINS: dict = {
        "AUT": CORS_ORIGINS_AUT,
        "LOCAL": CORS_ORIGINS_LOCAL,
        "STAGING": CORS_ORIGINS_STAGING,
        "PRODUCTION": CORS_ORIGINS_PRODUCTION,
        "DEVELOPMENT": CORS_ORIGINS_DEVELOPMENT,
    }

    ALLOW_CREDENTIALS: bool = getenv("ALLOW_CREDENTIALS", True)
