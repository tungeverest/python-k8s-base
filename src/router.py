import logging

from core.endpoints import auth, healths
from fastapi import APIRouter
from src.heros.endpoints import api as hero

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", status_code=200, tags=["INDEX"])
def index():
    return {"Hello": "World"}


print("__name__", __name__)

# CORE Routers
router.include_router(auth.router, prefix="/auth", tags=["AUTH"])
router.include_router(healths.router, prefix="/status", tags=["STATUS"])
# EXAMPLE MODULE
router.include_router(hero.router, prefix="/heroes", tags=["HEROES EXAMPLE"])

print("logger", logger)
logger.debug("123123")
