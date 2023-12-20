from os import getenv
from pydantic_settings import BaseSettings
from core.loggers.config import configure_logger


class LoggingConfig(BaseSettings):
    """
    NOTSET => DEBUG => INFO => WARNING => ERROR => CRITICAL
    """

    LOG_LEVEL: str = getenv("LOG_LEVEL", "INFO").upper()
    LOG_HANDLER: str = getenv("LOG_HANDLER", "default").lower()
    LOGGER_NAME: str = getenv("LOGGER_NAME", "").lower()
    LOG_PATH: str = getenv("LOG_PATH", "../../logs/log.txt")
    configure_logger(logger=LOGGER_NAME, level=LOG_LEVEL, file_path=LOG_PATH)
