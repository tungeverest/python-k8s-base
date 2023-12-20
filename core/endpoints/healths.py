import http

from core.configs.core import CoreSettings
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.setting import get_settings

router = APIRouter()


@router.get("/check-health", status_code=http.HTTPStatus.OK)
async def check_health(
    settings: CoreSettings = Depends(get_settings),
) -> JSONResponse:
    return JSONResponse(
        status_code=http.HTTPStatus.OK,
        content={
            "status": "OK",
            "name": settings.PROJECT_NAME,
            "version": settings.APP_VERSION,
        },
    )


@router.get("/liveness", status_code=http.HTTPStatus.OK)
async def liveness(
    settings: CoreSettings = Depends(get_settings),
) -> JSONResponse:
    return JSONResponse(
        status_code=http.HTTPStatus.OK,
        content={
            "status": "OK",
            "name": settings.PROJECT_NAME,
            "version": settings.APP_VERSION,
        },
    )


@router.get("/readiness", status_code=http.HTTPStatus.OK)
async def readiness(
    settings: CoreSettings = Depends(get_settings),
) -> JSONResponse:
    return JSONResponse(
        status_code=http.HTTPStatus.OK,
        content={
            "status": "OK",
            "name": settings.PROJECT_NAME,
            "version": settings.APP_VERSION,
        },
    )
