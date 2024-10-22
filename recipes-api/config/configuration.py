class SingletonMeta(type):
    """ Base class for singleton implementation. """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect the returned instance.
        """

        if cls not in cls._instances:

            instance = super().__call__(*args, **kwargs)

            cls._instances[cls] = instance

        return cls._instances[cls]


class RecipesConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton. """

    def __init__(self):
        """ Constructor that gets information from environment variables. """

        import os
        import sys
        import logging

        # Logging configuration
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)-5.5s]  %(message)s",
            handlers=[ logging.StreamHandler(sys.stdout) ]
        )
        self.logger = logging.getLogger()
        self.logger.info("Logger set successfully")

        # Recipes API configuration
        self.recipes_port = str('50000' if os.getenv('RECIPES_PORT') == None else os.getenv('RECIPES_PORT'))

        # Connection configuration
        self.api_url = "https://www.themealdb.com/api/json/v1/1"