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
from .db import engine, tarantool_db
from . import models
from .tarantool_loader import check_creating_spaces

models.Base.metadata.create_all(bind=engine)

# Add router in app
app.include_router(routes.router)

# Список спейсов Тарантула для каждого типа рекомендаций, а также исходных файлов.
spaces = [
    ['rec_test', 'events.csv', 'rec_test.json']
]

# Проверка инициализации спейса для каждой рекомендации. Если его нет, то создаем в Тарантуле
check_creating_spaces(spaces)

