from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api import settings
import tarantool

if settings.is_test:
    POSTGRES_DATABASE_URL = 'postgresql+psycopg2://{postgres_name}:{postgres_password}@{postgres_host}/{postgres_db}'.format(
        postgres_name=settings.postgres_name,
        postgres_password=settings.postgres_password,
        postgres_host=settings.postgres_host,
        postgres_db=settings.postgres_db_test
    )

    tarantool_db = tarantool.connect(settings.tarantool_host_test, settings.tarantool_port_test)

else:
    POSTGRES_DATABASE_URL = 'postgresql+psycopg2://{postgres_name}:{postgres_password}@{postgres_host}/{postgres_db}'.format(
        postgres_name=settings.postgres_name,
        postgres_password=settings.postgres_password,
        postgres_host=settings.postgres_host,
        postgres_db=settings.postgres_db
    )
    tarantool_db = tarantool.connect(settings.tarantool_host, settings.tarantool_port)

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

tarantool_db = tarantool.connect(settings.tarantool_host, settings.tarantool_port)
