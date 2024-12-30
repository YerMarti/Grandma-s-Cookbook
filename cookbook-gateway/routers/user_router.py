from fastapi import APIRouter
from requests import HTTPError

from models.user import User
from models.recipe import Recipe

from services.user_service import register_user, login_user, add_favorite_recipe, get_favorite_recipes

from config.configuration import GatewayConfiguration

config = GatewayConfiguration()

router = APIRouter()

@router.post("/register", summary="Registers a new user.", response_model=User)
async def register(username: str, password: str) -> User:
    """
    Registers a new user in the system.

    Parameters
    ----------
    username : str
        Username of the user.
    password : str
        Password of the user.
    
    Returns
    -------
    User
        User object with the registered data.
    """
    config.logger.debug(f"Request received to register user '{username}'.")
    user = None

    try:
        user = register_user(username, password)
    except HTTPError as e:
        config.logger.debug(f"Error registering user: {e}")
    
    config.logger.debug(f"Request to register user '{username}' processed succesfully.")
    return user


@router.post("/login", summary="Logs in a user.", response_model=User)
async def login(username: str, password: str) -> User:
    """
    Logs in a user in the system.

    Parameters
    ----------
    username : str
        Username of the user.
    password : str
        Password of the user.
    
    Returns
    -------
    User
        User object with the logged in data.
    """
    config.logger.debug(f"Request received to login user '{username}'.")
    user = None

    try:
        user = login_user(username, password)
    except HTTPError as e:
        config.logger.debug(f"Error logging in user: {e}")
    
    config.logger.debug(f"Request to login user '{username}' processed succesfully.")
    return user


@router.post("/{username}/favorite", summary="Adds a recipe to the user's favorites.", response_model=User)
async def favorite_recipe(username: str, recipe_id: str) -> User:
    """
    Adds a recipe to the user's favorite list.

    Parameters
    ----------
    username : str
        Username of the user.
    recipe_id : str
        Identifier of the recipe.
    
    Returns
    -------
    User
        User object with the updated favorite list.
    """
    config.logger.debug(f"Request received to add recipe '{recipe_id}' to user '{username}' favorites.")
    user = None

    try:
        user = add_favorite_recipe(username, recipe_id)
    except HTTPError as e:
        config.logger.debug(f"Error adding favorite recipe: {e}")
    
    config.logger.debug(f"Request to add recipe '{recipe_id}' to user '{username}' favorites processed succesfully.")
    return user


@router.get("/{username}/favorites", summary="Retrieves the user's favorite recipes.", response_model=list[Recipe])
async def favorites(username: str) -> list[Recipe]:
    """
    Retrieves the user's favorite recipes.

    Parameters
    ----------
    username : str
        Username of the user.
    
    Returns
    -------
    list[Recipe]
        A list of Recipe objects that are the user's favorites.
    """
    config.logger.debug(f"Request received to get favorite recipes for user '{username}'.")
    recipes = None

    try:
        recipes = get_favorite_recipes(username)
    except HTTPError as e:
        config.logger.debug(f"Error retrieving favorite recipes: {e}")
    
    config.logger.debug(f"Request to get favorite recipes for user '{username}' processed succesfully.")
    return recipes