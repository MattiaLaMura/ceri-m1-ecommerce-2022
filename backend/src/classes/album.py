# pylint: disable=too-few-public-methods, no-name-in-module
""" This file contains all the functions to get an album. """
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from database import Database


class Album(BaseModel):
    """ This class is used to stock an album. """
    album_id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int
    album_title: str
    album_year: date


def get_albums_from_artist(artist_id: int):
    """ This method gets all the albums of an artist.

    :return: The list of all the albums of the artist
    :rtype: list[Artist]
    """
    my_database = Database()
    albums = my_database.get_albums(str(artist_id))
    my_database.close()
    return [Album(**album) for album in albums]
