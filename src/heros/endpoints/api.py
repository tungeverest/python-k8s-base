import http

from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query, status
# from src.heros.endpoints.postgres import postgres_test

router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create A Hero who you want",  # API todo
    response_description="The Created Hero Successful Response",
)
async def create_hero(payload: dict):
    """
    Create an hero with property:

    - **name**: str required
    - **nickname**: str required
    - **age**: Optional[int]
    - **power**: int > 0 required
    """
    # postgres_test()
    return JSONResponse(
        status_code=http.HTTPStatus.OK,
        content={
            "status": "Create OK",
        },
    )


@router.get(
    "",
    status_code=200,
    summary="List Heros",  # API todo
    response_description="The Created Hero Successful Response",
)
async def list_heros(
    skip: int = Query(title="Offset Number of Page", ge=0, le=1000),
    end: int = Query(title="Limit Number each page", ge=10, le=100),
):  # Validate the returned data
    """
    List heros with:

    - **skip**: int > 0 < 1000 Offset of page (required)
    - **end**: int > 0 < 1000 limit each page (required)
    - **filters_params**: Optional[str]  ?param=value&param2=value2
    - **order**: Optional[str]
    """
    return JSONResponse(
        status_code=http.HTTPStatus.OK,
        content={
            "status": "List OK",
        },
    )
