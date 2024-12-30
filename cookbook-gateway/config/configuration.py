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


class GatewayConfiguration(metaclass=SingletonMeta):
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

        # Gateway API configuration
        self.gateway_port = str('50002' if os.getenv('GATEWAY_PORT') == None else os.getenv('GATEWAY_PORT'))

        # Recipe API configuration
        self.recipe_api_ip = str('localhost' if os.getenv('RECIPE_API_IP') == None else os.getenv('RECIPE_API_IP'))
        self.recipe_api_port = str('50000' if os.getenv('RECIPE_API_PORT') == None else os.getenv('RECIPE_API_PORT'))
        self.recipe_api_url = f"http://{self.recipe_api_ip}:{self.recipe_api_port}/recipes"
        self.logger.info(f"Recipe API URL: {self.recipe_api_url}")

        # Database configuration
        self.database_api_ip = str('localhost' if os.getenv('DATABASE_API_IP') == None else os.getenv('DATABASE_API_IP'))
        self.database_api_port = str('50001' if os.getenv('DATABASE_API_PORT') == None else os.getenv('DATABASE_API_PORT'))
        self.database_api_url = f"http://{self.database_api_ip}:{self.database_api_port}/users"
        self.logger.info(f"Database API URL: {self.database_api_url}")