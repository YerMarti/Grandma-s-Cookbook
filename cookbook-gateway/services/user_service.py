import requests
import json

from models.user import User
from models.recipe import Recipe

from config.configuration import GatewayConfiguration

config = GatewayConfiguration()


def register_user(username: str, password: str) -> User:
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
    config.logger.debug(f"Registering user with username '{username}'...")

    url = config.database_api_url + "/register"

    data = {
        "username": username,
        "password": password
    }

    request = requests.post(url=url, json=data)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    user = User.from_data(res)

    config.logger.debug(f"User '{user.username}' registered successfully.")
    return user


def login_user(username: str, password: str) -> User:
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
    config.logger.debug(f"Logging in user with username '{username}'...")

    url = config.database_api_url + "/login"

    data = {
        "username": username,
        "password": password
    }

    request = requests.post(url=url, json=data)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    user = User.from_data(res)

    config.logger.debug(f"User '{user.username}' logged in successfully.")
    return user


def add_favorite_recipe(username: str, recipe_id: str) -> User:
    """
    Adds a recipe to the user's favorite list.

    Parameters
    ----------
    user_id : str
        Identifier of the user.
    recipe_id : str
        Identifier of the recipe.
    
    Returns
    -------
    User
        User object with the updated data.
    """
    config.logger.debug(f"Adding recipe '{recipe_id}' to user '{username}' favorites...")

    url = config.database_api_url + f"/{username}/favorites"

    data = {
        "id": recipe_id
    }

    request = requests.post(url=url, json=data)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    user = User.from_data(res)

    config.logger.debug(f"Recipe '{recipe_id}' added to user '{username}' favorites successfully.")
    return user


def get_favorite_recipes(username: str) -> list[Recipe]:
    """
    Retrieves the favorite recipes of a user.

    Parameters
    ----------
    username : str
        Username of the user.
    
    Returns
    -------
    list
        List of Recipe objects.
    """
    config.logger.debug(f"Retrieving favorite recipes of user '{username}'...")

    url = config.database_api_url + f"/{username}/favorites"

    request = requests.get(url=url)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    recipes = [Recipe.from_data(recipe) for recipe in res]

    config.logger.debug(f"Favorite recipes of user '{username}' retrieved.")
    return recipes