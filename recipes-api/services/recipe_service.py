import requests

from models.recipe import Recipe

from config.configuration import RecipesConfiguration

config = RecipesConfiguration()


def search_recipe(name: str) -> list[Recipe]:
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
    url = config.api_url + "search.php"

    params = { "s": name }

    request = requests.get(url=url, params=params)
    request.raise_for_status()

    meals = request.content["meals"]

    if meals is None:
        return None
    
    recipes = [Recipe(meal) for meal in meals]

    return recipes


def get_recipe_details(id: str) -> Recipe:
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
    url = config.api_url + "lookup.php"

    params = { "i": id }

    request = requests.get(url=url, params=params)
    request.raise_for_status()

    meal = request.content["meals"]

    if meal is None:
        return None
    
    recipe = Recipe(meal[0])

    return recipe


def get_random_recipe() -> Recipe:
    """
    Gets a random recipe.

    Returns
    -------
    Recipe
        A Recipe object.
    """
    url = config.api_url + "random.php"

    request = requests.get(url=url)
    request.raise_for_status()

    meal = request.content["meals"]

    if meal is None:
        return None
    
    recipe = Recipe(meal[0])

    return recipe