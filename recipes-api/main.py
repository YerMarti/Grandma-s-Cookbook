from controller import app
from config.configuration import RecipesConfiguration

config = RecipesConfiguration()


if __name__ == "__main__":
    import uvicorn
    
    config.logger.info("Starting Cooking Recipes API")

    uvicorn.run(app, host="0.0.0.0", port=int(config.recipes_port))

    config.logger.info("Cooking Recipes API stopped")