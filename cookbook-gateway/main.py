from controller import app
from config.configuration import GatewayConfiguration

config = GatewayConfiguration()


if __name__ == "__main__":
    import uvicorn
    
    config.logger.info("Starting Cookbook Gateway API")

    uvicorn.run(app, host="0.0.0.0", port=int(config.gateway_port))

    config.logger.info("Cookbook Gateway API stopped")