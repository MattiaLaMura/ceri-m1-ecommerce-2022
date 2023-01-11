# pylint: disable=too-few-public-methods, no-name-in-module
""" This file contains all the functions to get an album. """
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from src.database.database import Database


class Album(BaseModel):
    """ This class is used to stock an album. """
    album_id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int
    album_title: str
    album_year: date
    album_image_url: str


def get_albums_from_artist(artist_id: int):
    """ This method gets all the albums of an artist.

    :return: The list of all the albums of the artist
    :rtype: list[Album]
    """
    my_database = Database()
    albums = my_database.get_albums(str(artist_id))
    my_database.close()
    return [Album(**album) for album in albums]


def get_all_albums():
    """ This method gets all the albums.

    :return: The list of all the albums
    :rtype: list[Album]
    """
    my_database = Database()
    albums = my_database.get_all_albums()
    my_database.close()
    return [Album(**album) for album in albums]


def get_album_from_id(album_id):
    """ This method gets an album by its id.

    :return: The album
    :rtype: Album
    """
    my_database = Database()
    album = my_database.get_album(str(album_id))
    my_database.close()
    return Album(**album)


def delete_album(album_id: int):
    """ This method removes an album from the database."""
    my_database = Database()
    album_deleted = my_database.delete_album(album_id)
    my_database.close()
    if album_deleted == 1:
        return True
    return False
