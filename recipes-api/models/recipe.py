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

        parameters
        ----------
        data : dict
            A dictionary containing the recipe data.

        Returns
        -------
        Recipe
            A Recipe instance.
        """        
        recipe_data = {
            "id": data["idMeal"],
            "name": data["strMeal"],
            "category": data["strCategory"],
            "area": data["strArea"],
            "instructions": data["strInstructions"],
            "thumbnail": data["strMealThumb"],
            "ingredients": {}
        }
        
        for i in range(1, 21):
            ingredient = f"strIngredient{i}"
            measure = f"strMeasure{i}"

            if data[ingredient] and data[measure]:
                recipe_data["ingredients"][data[ingredient]] = data[measure]

        return cls(**recipe_data)