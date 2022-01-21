from pydantic import BaseSettings


class Config_settings(BaseSettings):
    postgres_db: str
    postgres_name: str
    postgres_host: str
    postgres_password: str
    postgres_port: int
    tarantool_host: str
    tarantool_port: int

    # Test
    is_test: bool
    postgres_db_test: str
    tarantool_host_test: str
    tarantool_port_test: str

    class Config:
        env_file = ".env"
