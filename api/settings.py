from pydantic import BaseSettings


class Config_settings(BaseSettings):
    # Postgresql params
    postgres_db: str
    postgres_name: str
    postgres_host: str
    postgres_password: str
    postgres_port: int

    # Tarantool params
    tarantool_host: str
    tarantool_port: int
    tarantool_user: str
    tarantool_password: str

    # Test params
    is_test: bool
    postgres_db_test: str
    postgres_name_test: str
    postgres_host_test: str
    postgres_password_test: str
    postgres_port_test: int
    tarantool_host_test: str
    tarantool_port_test: str

    class Config:
        env_file = ".env"
