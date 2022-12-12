# pylint: disable=no-name-in-module, too-few-public-methods
""" This file contains all the functions to get and check an admin. """
from pydantic import BaseModel
from passlib.context import CryptContext
from src.database.database import Database

# To encode a password
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Admin(BaseModel):
    """ This class is used to stock an admin. """
    admin_id: int
    admin_name: str
    admin_password: str


def create_admin(admin_name, password):
    """ This method adds a new admin in the database.

    :param admin_name: The admin name
    :type admin_name: str
    :param password: The hashed password
    :type password: str
    """
    my_database = Database()
    my_database.add_admin(admin_name, password)
    my_database.close()


def get_admin(name: str):
    """ This method gets an admin by its name.

    :param name: The name of the admin
    :type name: str
    :return: The user object that has been found
    :rtype: user
    """
    my_database = Database()
    admin_info = my_database.get_admin_by_name(name)
    my_database.close()
    if admin_info:
        return Admin(**admin_info)
    return None


def authentication(name: str, password: str):
    """ This method checks if an admin is valid or not.

    :param name: The name of the admin
    :type name: str
    :param password: The password of the admin
    :type password: str
    :return: The admin if it exists, None if not
    :rtype: Admin
    """
    admin = get_admin(name)
    if not admin:
        return None
    if not verify_password(password, admin.admin_password):
        return None
    return admin


def get_password_hash(password):
    """ This method encodes a password.

    :param password: The password of the admin
    :type password: str
    :return: The hashed password
    :rtype: str
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """ This method checks if a password is valid or not.

    :param plain_password: The password of the admin
    :type plain_password: str
    :param hashed_password: The hashed password of the admin
    :type hashed_password: str
    :return: True if the password is valid, False if not
    """
    return pwd_context.verify(plain_password, hashed_password)
