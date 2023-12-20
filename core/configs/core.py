from os import getenv, path
from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    _ENV: str = getenv('_ENV')
    PORT: int = int(getenv('PORT', 8000))
    APP_VERSION: str = getenv("APP_VERSION", "")
    DESCRIPTION: str = getenv("DESCRIPTION", "")
    PROJECT_NAME: str = getenv("PROJECT_NAME", 'FASTAPI BASE')
    API_VERSION_PREFIX: str = getenv("API_VERSION_PREFIX", "/api/v1")
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    SWAGGER_URL: str = "/swagger.json"
    X_API_KEY: str = getenv("X_API_KEY")
    SECRET_KEY: str = getenv("SECRET_KEY")
    HOST: str = getenv('HOST')
    DEBUG: bool = getenv('DEBUG', False)
    ROOT_PROJECT: str = path.abspath(path.join(path.dirname(__file__), '../../'))
