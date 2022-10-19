""" This class is a database wrapper. It contains several
 functions to easily interact with the database. """
import mysql.connector as sql
from src.classes.environment_variable import Settings


class Database:
    """ This class contains all the functions interact with the database. """

    def __init__(self):
        """ The constructor from the Database class. When this constructor is called,
        a connection with the database is open. """
        # Open connection
        self.connection = sql.connect(user=Settings.USER,
                                      password=Settings.PASSWORD,
                                      host=Settings.HOST,
                                      dbname=Settings.DBNAME)
        # Create a cursor to perform database operations
        self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        """ This function allows to close the connection with the database. """
        self.connection.close()

    # Artist Table

    def get_artists(self):
        """ This method gets all the artists.

        :return: The list of all the artists
        :rtype: list[dict]
        """
        self.cursor.execute("SELECT * from artists")
        return self.cursor.fetchall()

    # Album Table

    def get_albums(self, artist_id: str):
        """ This method gets all the albums of an artist.

        :param artist_id: The artist id
        :type artist_id: str
        :return: The list of all the albums
        :rtype: list[dict]
        """
        self.cursor.execute("SELECT * from albums WHERE artist_id=%s", (artist_id, ))
        return self.cursor.fetchall()

    # Song Table

    def get_songs(self, album_id: str):
        """ This method gets all the songs of an album.

        :param album_id: The album id
        :type album_id: str
        :return: The list of all the songs
        :rtype: list[dict]
        """
        self.cursor.execute("SELECT * from songs WHERE album_id=%s", (album_id, ))
        return self.cursor.fetchall()
