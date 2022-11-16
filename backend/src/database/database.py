""" This class is a database wrapper. It contains several
 functions to easily interact with the database. """
import mysql.connector as sql
from environment_variable import Settings
from globals import DATABASE_FILE


class Database:
    """ This class contains all the functions interact with the database. """

    def __init__(self):
        """ The constructor from the Database class. When this constructor is called,
        a connection with the database is open. """
        # Open connection
        self.connection = sql.connect(user=Settings().dict()['user'],
                                      password=Settings().dict()['password'],
                                      host=Settings().dict()['host'],
                                      port=Settings().dict()['port'],
                                      database=Settings().dict()['dbname'])
        # Create a cursor to perform database operations
        self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        """ This function allows to close the connection with the database. """
        self.connection.close()

    # Init Functions
    def create_tables(self):
        """ This method creates the database. """
        with open(DATABASE_FILE, 'r', encoding='utf-8') as file:
            sql_file = file.read()
            file.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                if command.strip() != '':
                    self.cursor.execute(command)

    # Artist Table
    def add_artist(self, artist_name, is_active):
        """ This method adds a new artist. """
        self.cursor.execute(f'INSERT INTO artist(artist_name, is_active) '
                            f'VALUES ("{artist_name}", {is_active});')
        self.connection.commit()

    def get_artists(self):
        """ This method gets all the artists.

        :return: The list of all the artists
        :rtype: list[dict]
        """
        self.cursor.execute('SELECT * from artist')
        return self.cursor.fetchall()

    # Album Table
    def add_album(self, artist_id, album_title, album_year, album_cover):
        """ This method adds a new album. """
        self.cursor.execute('INSERT INTO album (artist_id, album_title, album_year, album_image_url) '
                            f'VALUES ((select artist_id FROM artist WHERE artist_id = {artist_id}), '
                            f'"{album_title}", "{album_year}", "{album_cover}");')
        self.connection.commit()

    def get_albums(self, artist_id: str):
        """ This method gets all the albums of an artist.

        :param artist_id: The artist id
        :type artist_id: str
        :return: The list of all the albums
        :rtype: list[dict]
        """
        self.cursor.execute(
            'SELECT * from album WHERE artist_id=%s', (artist_id,))
        return self.cursor.fetchall()

    # Song Table
    def add_song(self, album_id, song_title, song_length):
        """ This method adds a new song. """
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id = '
                            f'{album_id}), "{song_title}", {song_length});')
        self.connection.commit()

    def get_songs(self, album_id: str):
        """ This method gets all the songs of an album.

        :param album_id: The album id
        :type album_id: str
        :return: The list of all the songs
        :rtype: list[dict]
        """
        self.cursor.execute(
            'SELECT * from song WHERE album_id=%s', (album_id,))
        return self.cursor.fetchall()
