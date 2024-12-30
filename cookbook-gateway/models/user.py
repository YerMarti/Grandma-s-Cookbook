from pydantic import BaseModel

from models.recipe import Recipe

class User(BaseModel):
    """
    Base class for a user.

    Attributes
    ----------
    username : str
        The username of the user.
    password : str
        The password of the user.
    favoriteRecipes : list[Recipe]
        A list of Recipe objects that the user has marked as favorite.
    """
    
    username: str

    password: str

    favoriteRecipes: list[Recipe]


    @classmethod
    def from_data(cls, data: dict):
        """
        Creates a User instance from a given data dictionary.

        Parameters
        ----------
        data : dict
            A dictionary containing the user data.

        Returns
        -------
        Recipe
            A User instance.
        """
        user_data = {
            "username": data["username"],
            "password": data["password"],
            "favoriteRecipes": data["favoriteRecipes"]
        }

        return cls(**user_data)