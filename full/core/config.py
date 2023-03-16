from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    """ 
        debug: bool
        project_name: str
        version: str
        description: str """

    # Database
    ASYNC_CONN_STR: str
    # env
    class Config:
        env_file = ".env"

settings = Settings()
