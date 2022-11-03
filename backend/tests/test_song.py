""" Unit tests for all the methods of the src.classes.song file. """
from unittest.mock import Mock
from src.classes import song


def test_get_songs_from_album(self, mock_get_songs_from_album, songs):
    """ Unit tests for the get_all_artists method. """
    self.assertEqual(len(mock_get_songs_from_album()), 2)
    self.assertEqual(type(mock_get_songs_from_album()), list)
    self.assertEqual(type(mock_get_songs_from_album()[0]), song.Song)
    self.assertEqual(mock_get_songs_from_album(), songs)


def run_tests(self):
    """ Function to run all the tests for the src.classes.artist methods. """
    song.get_songs_from_album = Mock()
    song_object = song.Song(**{'song_id': 0, 'album_id': 0, 'song_title': 'test',
                               'song_length': 213})
    songs = [song_object, song_object]
    song.get_songs_from_album.return_value = songs
    test_get_songs_from_album(self, song.get_songs_from_album, songs)
