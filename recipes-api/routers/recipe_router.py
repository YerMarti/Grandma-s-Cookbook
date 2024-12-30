from fastapi import APIRouter
from requests import HTTPError

from models.recipe import Recipe

from services.recipe_service import get_recipes_by_name, get_recipe_by_id, get_random_recipe

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()
router = APIRouter()

@router.get("/search-recipe", summary="Retrieves a list of recipes that match the name.")
async def search_recipe(name: str) -> list[Recipe]:
    """
    Retrieves a list of recipes that match the name.

    Parameters
    ----------
    name : str
        Name to query for.
    
    Returns
    -------
    list[Recipe]
        A list of Recipe objects that match the query name.
    """
    recipes = None

    try:
        recipes = get_recipes_by_name(name)
    except HTTPError as e:
        config.logger.debug(f"Error searching for recipes: {e}")
    
    return recipes

@router.get("/{id}", summary="Retrieves all the details of a given recipe.")
async def recipe_details(id: str) -> Recipe:
    """
    Retrieves all the details of a given recipe.

    Parameters
    ----------
    id : str
        Identifier of the recipe.
    
    Returns
    -------
    Recipe
        A Recipe object with the requested id.
    """
    recipe = None

    try:
        recipe = get_recipe_by_id(id)
    except HTTPError as e:
        config.logger.debug(f"Error retrieving recipe: {e}")
    
    return recipe

@router.get("/random-recipe", summary="Gets a random recipe.")
async def random_recipe() -> Recipe:
    """
    Gets a random recipe.

    Returns
    -------
    Recipe
        A Recipe object.
    """
    recipe = None

    try:
        recipe = get_recipe_by_id(id)
    except HTTPError as e:
        config.logger.debug(f"Error retrieving recipe: {e}")
    
    return recipe