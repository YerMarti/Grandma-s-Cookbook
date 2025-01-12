from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers.recipe_router import router as RecipeRouter
from routers.user_router import router as UserRouter

from config.configuration import GatewayConfiguration

config = GatewayConfiguration()

tags_metadata = [
    {
        "name": "Recipes",
        "description": "Operations with cooking recipes.",
    },
    {
        "name": "Users",
        "description": "Operations with users.",
    },
]

description = """
The **Cookbook Gateway API** manages different operations including recipes for cooking and users.
"""

app = FastAPI(
    title="Cookbook Gateway API",
    description=description,
    summary="Cookbook Gateway API for the project",
    version="0.1",
    openapi_tags=tags_metadata
)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RecipeRouter, tags=["Recipes"], prefix=f"/recipes")
app.include_router(UserRouter, tags=["Users"], prefix=f"/users")

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')