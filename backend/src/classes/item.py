# pylint: disable=no-name-in-module, too-few-public-methods
""" This file contains all the functions to add, get and remove an item. """
from pydantic import BaseModel
from src.database.database import Database


class Item(BaseModel):
    """ This class is used to stock an item. """
    item_id: int
    album_id: int
    user_id: int
    paid: bool
    delivery: str


def create_item(album_id: int, user_id: int, paid: bool):
    """ This method adds a new item in the database.

    :param user_id: The user id
    :type user_id: int
    :param album_id: The album id
    :type album_id: int
    :param paid: if the item is still on the cart or not
    :type paid: bool
    """
    my_database = Database()
    my_database.add_item(album_id, user_id, paid)
    my_database.close()


def get_items(user_id: int):
    """ This method gets all the items information.

    :param user_id: The user id
    :type user_id: int
    :return: The list of all the items in the database
    :rtype: list[Item]
    """
    my_database = Database()
    items = my_database.get_items(user_id)
    my_database.close()
    return [Item(**item) for item in items]


def buy_item(item_id: int, user_id: int):
    """ This method adds a new item in the database.

    :param user_id: The user id
    :type user_id: int
    :param item_id: The item id
    :type item_id: int
    """
    my_database = Database()
    item_bought = my_database.buy_item(item_id, user_id)
    my_database.close()
    if item_bought == 1:
        return True
    return False


def delete_item(item_id: int, user_id: int):
    """ This method removes an item from the database.

    param user_id: The user id
    :type user_id: int
    :param item_id: The id of the item that will be removed
    :type item_id: int
    :return: True if the item has been deleted, False if not
    :rtype: bool
    """
    my_database = Database()
    item_deleted = my_database.delete_item(item_id, user_id)
    my_database.close()
    if item_deleted == 1:
        return True
    return False


def update_item(item_id: int, user_id: int, status: str):
    """ This method updates an item in the database.

    :param user_id: The user id
    :type user_id: int
    :param item_id: The item id
    :type item_id: int
    :param status: The status of the order
    :type status: str
    """
    my_database = Database()
    item_updated = my_database.update_item(item_id, user_id, status)
    my_database.close()
    if item_updated == 1:
        return True
    return False
