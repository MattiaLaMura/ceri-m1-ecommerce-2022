# pylint: disable=too-few-public-methods, no-name-in-module
""" This file contains all the functions to get a song. """
from typing import Optional
from pydantic import BaseModel, Field
from src.database.database import Database


class Song(BaseModel):
    """ This class is used to stock a song. """
    song_id: Optional[int] = Field(default=None, primary_key=True)
    album_id: int
    song_title: str
    song_length: int


def get_songs_from_album(album_id: int):
    """ This method gets all the songs of an album.

    :return: The list of all the songs of the album
    :rtype: list[Song]
    """
    my_database = Database()
    songs = my_database.get_songs(str(album_id))
    my_database.close()
    return [Song(**song) for song in songs]


def get_all_songs():
    """ This method gets all the songs.

    :return: The list of all the songs
    :rtype: list[Song]
    """
    my_database = Database()
    songs = my_database.get_all_songs()
    my_database.close()
    return [Song(**song) for song in songs]
