from fastapi import APIRouter

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()
router = APIRouter()

@router.post("/", summary="")
async def smth():
    pass