# pylint: disable=too-few-public-methods, no-name-in-module
""" This file contains all the functions to get an artist. """
from pydantic import BaseModel, Field
from src.database.database import Database


class Artist(BaseModel):
    """ This class is used to stock a artist. """
    artist_id: int = Field(default=None, primary_key=True)
    artist_name: str
    is_active: bool


def get_all_artists():
    """ This method gets all the artists.

    :return: The list of all the artists
    :rtype: list[Artist]
    """
    my_database = Database()
    artists = my_database.get_artists()
    my_database.close()
    return [Artist(**artist) for artist in artists]
