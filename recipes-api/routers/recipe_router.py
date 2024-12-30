from fastapi import APIRouter
from requests import HTTPError

from models.recipe import Recipe

from services.recipe_service import get_recipes_by_name, get_recipe_by_id, get_random_recipe

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()
router = APIRouter()


@router.get("/search", summary="Retrieves a list of recipes that match the name.", response_model=list[Recipe])
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
    config.logger.debug(f"Request received to search '{name}'.")
    recipes = None

    try:
        recipes = get_recipes_by_name(name)
    except HTTPError as e:
        config.logger.debug(f"Error searching for recipes: {e}")
    
    config.logger.debug(f"Request to search '{name}' processed succesfully.")
    return recipes


@router.get("/random", summary="Gets a random recipe.", response_model=Recipe)
async def random_recipe() -> Recipe:
    """
    Gets a random recipe.

    Returns
    -------
    Recipe
        A Recipe object.
    """
    config.logger.debug(f"Request received to get a random recipe.")
    recipe = None

    try:
        recipe = get_random_recipe()
    except HTTPError as e:
        config.logger.debug(f"Error retrieving recipe: {e}")
    
    config.logger.debug(f"Request to get a random recipe processed succesfully.")
    return recipe


@router.get("/{id}", summary="Retrieves all the details of a given recipe.", response_model=Recipe)
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
    config.logger.debug(f"Request received to get details of recipe with id '{id}'.")
    recipe = None

    try:
        recipe = get_recipe_by_id(id)
    except HTTPError as e:
        config.logger.debug(f"Error retrieving recipe: {e}")
    
    config.logger.debug(f"Request to get details of recipe with id '{id}' processed succesfully.")
    return recipe