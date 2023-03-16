"""Module orm"""
from os import getenv

from dotenv import load_dotenv

from .config import Settings
from .db import Base, async_engine


load_dotenv(getenv(".env"))

settings = Settings()
