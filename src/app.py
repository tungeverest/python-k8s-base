import logging
from os import getenv

from core.middlewares.https.process_time import process_time_log_middleware
from core.middlewares.https.rate_limit import RateLimitCoreMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from src.router import router as api_router
from src.setting import get_settings


logger = logging.getLogger(__name__)


def create_app():
    settings = get_settings()
    app = FastAPI(
        title=f"{settings.PROJECT_NAME}",
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        description=f"""
        FastAPI Framework + K8s \n
          - PROJECT NAME: {settings.PROJECT_NAME} \n
          - VERSION: {settings.APP_VERSION} \n
          - ENV: {settings._ENV} \n
          - DEBUG: {settings.DEBUG} \n
          - API URI: {settings.API_VERSION_PREFIX} \n
        """,
    )
    app.include_router(api_router, prefix=settings.API_VERSION_PREFIX)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=settings.cors.ALLOW_METHODS,
        allow_headers=settings.cors.ALLOW_HEADERS,
        allow_origins=settings.cors.CORS_ORIGINS.get(getenv("_ENV")),
        max_age=settings.cors.MAX_AGE_CACHE,
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.cors.TRUSTED_HOST,
    )
    app.add_middleware(RateLimitCoreMiddleware)
    app.middleware("http")(process_time_log_middleware)

    @app.on_event("startup")
    async def on_startup():
        logging.info("Startup Event Triggered")

    @app.on_event("shutdown")
    async def on_shutdown():
        logging.info("Shutdown Event Triggered")

    print("+++++++++++++++++++", getenv("_ENV"))
    return app, settings
