from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Base class for a recipe.

    Attributes
    ----------
    id : str
        Identifier of the recipe.
    name : str
        Name of the recipe.
    category : str
        The category the recipe belongs to.
    area : str
        The country/region the recipe is original from.
    instructions : str
        Text containing the instructions to follow in order to prepare the meal.
    thumbnail : str
        URL to an image of the meal.
    ingredients : dict[str, str]
        Dictionary containing the ingredients and measures necessary to prepare the recipe.
    """

    id: str
    
    name: str

    category: str

    area: str

    instructions: str

    thumbnail: str

    ingredients: dict[str, str]


    @classmethod
    def from_data(cls, data: dict):
        """
        Creates a Recipe instance from a given data dictionary.

        Parameters
        ----------
        data : dict
            A dictionary containing the recipe data.

        Returns
        -------
        Recipe
            A Recipe instance.
        """        
        recipe_data = {
            "id": data["id"],
            "name": data["name"],
            "category": data["category"],
            "area": data["area"],
            "instructions": data["instructions"],
            "thumbnail": data["thumbnail"],
            "ingredients": data["ingredients"]
        }

        return cls(**recipe_data)