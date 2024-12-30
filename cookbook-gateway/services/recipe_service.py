import requests
import json

from models.recipe import Recipe

from config.configuration import GatewayConfiguration

config = GatewayConfiguration()


def get_recipes_by_name(name: str) -> list[Recipe]:
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
    config.logger.debug(f"Searching recipes with name '{name}'...")

    params = { "name": name }
    url = config.recipe_api_url + "/search"

    request = requests.get(url=url, params=params)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    if res is None or len(res) == 0:
        config.logger.debug("No recipes found.")
        return None
    
    recipes = [Recipe.from_data(data) for data in res]

    config.logger.debug(f"{len(recipes)} recipes found.")
    return recipes


def get_recipe_by_id(id: str) -> Recipe:
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
    config.logger.debug(f"Retrieving recipe with id '{id}'...")

    url = config.recipe_api_url + f"/{id}"

    request = requests.get(url=url)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    if res is None:
        config.logger.debug("No recipe found.")
        return None
    
    recipe = Recipe.from_data(res)

    config.logger.debug("Recipe retrieved.")
    return recipe


def get_random_recipe() -> Recipe:
    """
    Gets a random recipe.

    Returns
    -------
    Recipe
        A Recipe object.
    """
    config.logger.debug("Retrieving a random recipe...")

    url = config.recipe_api_url + "/random"

    request = requests.get(url=url)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))

    if res is None:
        config.logger.debug("No recipe found.")
        return None
    
    recipe = Recipe.from_data(res)

    config.logger.debug("Random recipe retrieved.")
    return recipe