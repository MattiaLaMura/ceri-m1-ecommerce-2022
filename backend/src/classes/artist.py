# pylint: disable=too-few-public-methods
""" This file contains all the functions to get an artist. """
from pydantic import BaseModel, Field


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
    return ['a', 'b', 'c']
