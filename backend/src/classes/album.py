# pylint: disable=too-few-public-methods
""" This file contains all the functions to get an album. """
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date
from database import Database


class Album(BaseModel):
    """ This class is used to stock an album. """
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int
    name: str
    year: date


def get_albums_from_artist(artist_id: int):
    """ This method gets all the albums of an artist.

    :return: The list of all the albums of the artist
    :rtype: list[Artist]
    """
    my_database = Database()
    albums = my_database.get_albums(str(artist_id))
    my_database.close()
    return [Album(**album) for album in albums]
