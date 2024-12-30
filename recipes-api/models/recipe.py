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


    def __init__(self, data: dict):
        self.id = data["idMeal"]
        self.name = data["strMeal"]
        self.category = data["strCategory"]
        self.area = data["strArea"]
        self.instructions = data["strInstructions"]
        self.thumbnail = data["strMealThumb"]
        self.ingredients = {}
        
        for i in range(1, 21):
            ingredient = f"strIngredient{i}"
            measure = f"strMeasure{i}"

            if data[ingredient] is None and data[ingredient] != "":
                break

            self.ingredients[data[ingredient]] = data[measure]