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

    def fill_tables(self):
        """ This method fills the database. """
        self.fill_artist_table()
        self.fill_album_table()
        self.fill_song_table()
        self.connection.commit()

    # Artist Table
    def fill_artist_table(self):
        """ This method fills the artist table. """
        self.cursor.execute(
            'INSERT INTO artist(artist_name, is_active) VALUES ("Lorenzo", true);')
        self.cursor.execute(
            'INSERT INTO artist(artist_name, is_active) VALUES ("Mattia", false);')
        self.cursor.execute(
            'INSERT INTO artist(artist_name, is_active) VALUES ("Bastien", true);')

    def get_artists(self):
        """ This method gets all the artists.

        :return: The list of all the artists
        :rtype: list[dict]
        """
        self.cursor.execute('SELECT * from artist')
        return self.cursor.fetchall()

    # Album Table
    def fill_album_table(self):
        """ This method fills the album table. """
        image_1 = 'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/99bd31fd-b68e-4fa6-b351-62173827ac21/67.jpg'
        image_2 = 'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/6b2ef062-6913-4a94-a265-7d75f4f91854/64.jpg'
        image_3 = 'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/e2f9aa74-7587-4a30-b0c0-4df61d7ac308/43.jpg'
        self.cursor.execute('INSERT INTO album (artist_id, album_title, album_year, album_image_url) '
                            'VALUES ((select artist_id FROM artist WHERE artist_id '
                            '= 1), "Album de Lorenzo", "2022-10-21", "' + image_1 + '");')
        self.cursor.execute('INSERT INTO album (artist_id, album_title, album_year, album_image_url) '
                            'VALUES ((select artist_id FROM artist WHERE artist_id '
                            '= 2), "Album de Mattia", "2018-12-06", "' + image_2 + '");')
        self.cursor.execute('INSERT INTO album (artist_id, album_title, album_year, album_image_url) '
                            'VALUES ((select artist_id FROM artist WHERE artist_id '
                            '= 3), "Album de Bastien", "2021-01-13", "' + image_3 + '");')

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
    def fill_song_table(self):
        """ This method fills the song table. """
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 1), "Song 1", 153);')
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 1), "Song 2", 121);')
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 2), "Song 1", 153);')
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 2), "Song 2", 121);')
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 3), "Song 1", 153);')
        self.cursor.execute('INSERT INTO song (album_id, song_title, song_length) '
                            'VALUES ((select album_id FROM album WHERE album_id '
                            '= 3), "Song 2", 121);')

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
