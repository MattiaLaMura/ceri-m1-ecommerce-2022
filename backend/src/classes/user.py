# pylint: disable=no-name-in-module, too-few-public-methods
""" This file contains all the functions to add, get and check an user. """
# from validate_email import validate_email
from pydantic import BaseModel
from passlib.context import CryptContext
from src.database.database import Database

# To encode a password
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class User(BaseModel):
    """ This class is used to stock a user. """
    user_id: int
    user_name: str
    user_email: str
    user_password: str


def create_user(user_name, user_email, password):
    """ This method adds a new user in the database.

    :param user_email: The user email
    :type user_email: str
    :param user_name: The username
    :type user_name: str
    :param password: The hashed password
    :type password: str
    """
    my_database = Database()
    my_database.add_user(user_email, user_name, password)
    my_database.close()


def get_users():
    """ This method gets all the users information.

    :return: The list of all the users in the database
    :rtype: list[User]
    """
    my_database = Database()
    user_info = my_database.get_users()
    my_database.close()
    return [User(**user) for user in user_info]


def get_user(email: str):
    """ This method gets a user by its email.

    :param email: The email of the user
    :type email: str
    :return: The user object that has been found
    :rtype: user
    """
    my_database = Database()
    user_info = my_database.get_user_by_email(email)
    my_database.close()
    if user_info:
        return User(**user_info)
    return None


def authentication(email: str, password: str):
    """ This method checks if a user is valid or not.

    :param email: The email of the user
    :type email: str
    :param password: The password of the user
    :type password: str
    :return: The user if it exists, None if not
    :rtype: User
    """
    user = get_user(email)
    if not user:
        return None
    if not verify_password(password, user.user_password):
        return None
    return user


def get_password_hash(password):
    """ This method encodes a password.

    :param password: The password of the user
    :type password: str
    :return: The hashed password
    :rtype: str
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """ This method checks if a password is valid or not.

    :param plain_password: The password of the user
    :type plain_password: str
    :param hashed_password: The hashed password of the user
    :type hashed_password: str
    :return: True if the password is valid, False if not
    """
    return pwd_context.verify(plain_password, hashed_password)


def verify_email(email):
    """ This method checks if an email is valid or not.

    :param email: The email of the user
    :type email: str
    :return: bool
    :rtype: True if the email is valid, False if not
    """
    my_database = Database()
    exist = my_database.get_email_by_email(email)
    my_database.close()
    if exist:
        return False  # If the email is already in the database
    # if not validate_email(email, verify=True):
        # return False  # Email not valid
    return True
