""" Unit tests for all the methods of the src.classes.artist file. """
from unittest.mock import Mock
from src.classes import artist


def test_get_all_artists(self, mock_get_all_artists, artists):
    """ Unit tests for the get_all_artists method. """
    self.assertEqual(len(mock_get_all_artists()), 2)
    self.assertEqual(type(mock_get_all_artists()), list)
    self.assertEqual(type(mock_get_all_artists()[0]), artist.Artist)
    self.assertEqual(mock_get_all_artists(), artists)


def run_tests(self):
    """ Function to run all the tests for the src.classes.artist methods. """
    artist.get_all_artists = Mock()
    artist_object = artist.Artist(**{'artist_id': 0, 'artist_name': 'test', 'is_active': True})
    artists = [artist_object, artist_object]
    artist.get_all_artists.return_value = artists
    test_get_all_artists(self, artist.get_all_artists, artists)
