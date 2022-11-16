# pylint: disable=too-few-public-methods
""" This file contains the class to stock the environment variables. """
from pydantic import BaseSettings
from environment_variable import Settings


class Settings(BaseSettings):
    """ This class is used to stock the environment variables. """
    user: str
    password: str
    host: str
    port: str
    dbname: str
    secret_key: str
