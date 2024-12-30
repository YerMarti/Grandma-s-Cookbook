import requests
import json

from models.recipe import Recipe

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()


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
    url = config.api_url + "/search.php"

    params = { "s": name }

    request = requests.get(url=url, params=params)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))
    meals = res["meals"]

    if meals is None or len(meals) == 0:
        config.logger.debug("Could not find any recipes.")
        return None
    
    recipes = [Recipe.from_data(meal) for meal in meals]

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
    url = config.api_url + "/lookup.php"

    params = { "i": id }

    request = requests.get(url=url, params=params)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))
    meal = res["meals"]

    if meal is None or len(meal) == 0:
        config.logger.debug("Recipe not found.")
        return None
    
    recipe = Recipe.from_data(meal[0])

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
    url = config.api_url + "/random.php"

    request = requests.get(url=url)
    request.raise_for_status()

    res = json.loads(request.content.decode("utf-8"))
    meal = res["meals"]

    if meal is None or len(meal) == 0:
        config.logger.debug("Could not find a recipe.")
        return None
    
    recipe = Recipe.from_data(meal[0])

    config.logger.debug("Random recipe retrieved.")
    return recipe