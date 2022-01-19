from fastapi import FastAPI
from .settings import Config_settings
from logging.config import dictConfig
import logging
from .config_logs import LogConfig

# initial settings
settings = settings.Config_settings()

# initial app
app = FastAPI()

# initial logger
dictConfig(LogConfig().dict())
logger = logging.getLogger("pushka")

from api import routes

# Add router in app
app.include_router(routes.router)

