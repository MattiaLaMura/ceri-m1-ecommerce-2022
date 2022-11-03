""" Unit Tests for all the Backend functions. """
import unittest
from tests import test_run_backend, test_artist, test_album, test_song


class TestStringMethods(unittest.TestCase):
    """ This class runs all the tests of the different functions of the Backend. """

    def test_run_backend(self):
        """ Unit tests for all the test_run_backend functions. """
        test_run_backend.run_tests(self)

    def test_artist(self):
        """ Unit tests for all the test_artist functions. """
        test_artist.run_tests(self)

    def test_album(self):
        """ Unit tests for all the test_album functions. """
        test_album.run_tests(self)

    def test_song(self):
        """ Unit tests for all the test_song functions. """
        test_song.run_tests(self)


if __name__ == '__main__':
    # Run tests
    unittest.main()
