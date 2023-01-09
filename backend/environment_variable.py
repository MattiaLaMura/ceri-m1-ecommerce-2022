# pylint: disable=too-few-public-methods
""" This file contains the class to stock the environment variables. """
from pydantic import BaseSettings


class Settings(BaseSettings):
    """ This class is used to stock the environment variables. """
    user: str
    password: str
    host: str
    mysql_port: str
    dbname: str
    secret_key: str
    algolia_application_id: str
    algolia_api_key: str
    algolia_index_name: str
