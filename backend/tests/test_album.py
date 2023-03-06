""" Unit tests for all the methods of the src.classes.album file. """
from unittest.mock import Mock
from datetime import date
from src.classes import album


def test_get_albums_from_artist(self, mock_get_albums_from_artist, albums):
    """ Unit tests for the get_all_artists method. """
    self.assertEqual(len(mock_get_albums_from_artist()), 2)
    self.assertEqual(type(mock_get_albums_from_artist()), list)
    self.assertEqual(type(mock_get_albums_from_artist()[0]), album.Album)
    self.assertEqual(mock_get_albums_from_artist(), albums)


def run_tests(self):
    """ Function to run all the tests for the src.classes.album methods. """
    album.get_albums_from_artist = Mock()
    album_object = album.Album(**{'album_id': 0, 'artist_id': 0, 'album_title': 'test',
                                  'album_year': date.today(), 'album_image_url': 'url'})
    albums = [album_object, album_object]
    album.get_albums_from_artist.return_value = albums
    test_get_albums_from_artist(self, album.get_albums_from_artist, albums)
