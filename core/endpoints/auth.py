import http

from core.configs.core import CoreSettings
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.setting import get_settings

router = APIRouter()


@router.get("/local/x-api-key", status_code=http.HTTPStatus.OK)
async def readiness(
    settings: CoreSettings = Depends(get_settings),
) -> JSONResponse:
    if settings._ENV == "LOCAL":
        return JSONResponse(
            status_code=http.HTTPStatus.OK,
            content={
                "status": "OK",
                "x-api-key": settings.X_API_KEY,
            },
        )

    return JSONResponse(
        status_code=401,
        content={
            "status": "Not Local",
            "x-api-key": None,
        },
    )
