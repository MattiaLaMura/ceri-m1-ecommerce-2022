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

    # User Table
    def add_user(self, user_email, user_name, user_password):
        """ This method adds a new user in the database.

        :param user_email: The user email
        :type user_email: str
        :param user_name: The user name
        :type user_name: str
        :param user_password: The hashed password of the user
        :type user_password: str
        """
        self.cursor.execute('INSERT into user (user_email, user_name, user_password) values '
                            '(%s, %s, %s)', (user_email, user_name, user_password))
        self.connection.commit()

    def get_users(self):
        """ This method gets all the users from the database.

        :return: The list of all the users
        :rtype: list[dict]
        """
        self.cursor.execute('SELECT * from user')
        return self.cursor.fetchall()

    def get_user_by_email(self, email):
        """ This method gets a user using an email.

        :param email: The User email
        :type email: str
        :return: The user information
        :rtype: dict
        """
        self.cursor.execute('SELECT * from user WHERE user_email = %s', (email,))
        user = self.cursor.fetchone()
        return user

    def get_email_by_email(self, email):
        """ This method gets an email using an email.
        This is used to check if an email is valid or not.

        :return: The user email that has been found
        :rtype: dict
        """
        self.cursor.execute(
            'SELECT user_email from user WHERE user_email = %s', (email,))
        return self.cursor.fetchone()

    # Item Table
    def add_item(self, album_id, user_id, paid):
        """ This method adds a new item in the database.

        :param user_id: The user id
        :type user_id: int
        :param album_id: The album id
        :type album_id: int
        :param paid: if the item is still on the cart or not
        :type paid: bool
        """
        self.cursor.execute('INSERT INTO item (album_id, user_id, paid) '
                            f'VALUES ((select album_id FROM album WHERE album_id = {album_id}), '
                            f'(select user_id FROM user WHERE user_id = {user_id}), {paid});')
        self.connection.commit()

    def get_items(self, user_id: int):
        """ This method gets all the items information.

        :param user_id: The user id
        :type user_id: int
        """
        self.cursor.execute(f'SELECT * from item where user_id = {user_id}')
        return self.cursor.fetchall()

    def buy_item(self, item_id: int, user_id: int):
        """ This method adds a new item in the database.

        :param user_id: The user id
        :type user_id: int
        :param item_id: The item id
        :type item_id: int
        """
        self.cursor.execute(f'UPDATE item SET paid = TRUE WHERE user_id = {user_id}'
                            f' and item_id = {item_id}')
        self.connection.commit()
        return self.cursor.rowcount

    def delete_item(self, item_id: int, user_id: int):
        """ This method removes an item from the database.

        :param user_id: The id of the user, owner of the item
        :type user_id: int
        :param item_id: The id of the item that will be removed
        :type item_id: int
        :return: 1 if the user has been deleted, 0 if not
        :rtype: int
        """
        self.cursor.execute(f'DELETE from item WHERE user_id = {user_id}'
                            f' and item_id = {item_id}')
        self.connection.commit()
        return self.cursor.rowcount
