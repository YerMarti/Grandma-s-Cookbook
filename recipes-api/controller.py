from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.recipe_router import router as RecipeRouter

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()

tags_metadata = [
    {
        "name": f"Recipes",
        "description": f"Operations with cooking recipes.",
    },
]

description = f"""
The **Cooking Recipes API** manages different operations including recipes for cooking.
"""

app = FastAPI(
    title="Cooking Recipes API",
    description=description,
    summary="Cooking Recipes API for the project",
    version="0.1",
    openapi_tags=tags_metadata
)

app.include_router(RecipeRouter, tags=["Recipes"], prefix=f"/recipes")

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')