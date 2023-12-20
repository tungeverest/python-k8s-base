from os import getenv
from functools import lru_cache
from core.configs.core import CoreSettings
from pydantic_settings import BaseSettings

from core.configs.sql import DBConfig
from core.configs.auth import AuthConfig
from core.configs.cors import CorsConfig
from core.configs.logging import LoggingConfig


# Decorator for cache
@lru_cache()
def get_settings() -> CoreSettings:
    if getenv("_ENV", None) is None:
        raise Exception("Cannot get _ENV environment")
    return CustomSettings()


class CustomSettings(CoreSettings):
    db: BaseSettings = DBConfig()
    cors: BaseSettings = CorsConfig()
    auth: BaseSettings = AuthConfig()
    logging: BaseSettings = LoggingConfig()
