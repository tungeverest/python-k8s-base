from os import getenv
from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    X_API_KEY: str = getenv("X_API_KEY", "")

    # JWT
    SECRET_KEY: str = getenv("SECRET_KEY", "")
    SECURITY_ALGORITHM: str = "HS256"
    # Token expired after 7 days
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
