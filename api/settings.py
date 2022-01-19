from pydantic import BaseSettings


class Config_settings(BaseSettings):
    is_test: bool

    class Config:
        env_file = ".env"
