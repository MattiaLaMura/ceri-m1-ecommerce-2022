# pylint: disable=no-name-in-module, too-few-public-methods
""" This file contains all the functions to generate and encode a Token. """
from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from globals import ALGORITHM
from environment_variable import Settings
from src.classes.user import get_user
from src.classes.admin import get_admin

# The dependency for the oauth2.0 authorisation when the token is passed
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class Token(BaseModel):
    """ This class is used to stock an access token and its type. """
    access_token: str
    token_type: str


def create_access_token(data: dict, expires_delta: timedelta):
    """ This method creates a JWT token using the current user info.

   :param data: A dict containing the user info that will be added into the token
   :type data: dict
   :param expires_delta: The expiration date of the token
   :type expires_delta: timedelta
   :return: The JWT token conteining an expiration date and the user info
   :rtype: str
   """
    expire = datetime.utcnow() + expires_delta
    data.update({'exp': expire})
    encoded_jwt = jwt.encode(data, Settings().dict()['secret_key'],
                             algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    """ This method decodes the JWT token to get the current user.

    :param token: The token that have to be decoded to get the current user
    :type token: str
    :raises HTTPException: If the token is not valid
    :return: The current user
    :rtype: User
    """
    try:
        payload = jwt.decode(token, Settings().dict()['secret_key'],
                             algorithms=[ALGORITHM])
        email = payload.get('email')
        if email is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The token is not valid.')
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='JWTError: the token cannot be decoded.') from exc
    user = get_user(email=email)
    if user is None:
        if email is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The user contained in the token is not valid.')
    return user


def get_current_admin(token: str = Depends(oauth2_scheme)):
    """ This method decodes the JWT token to get the current admin.

    :param token: The token that have to be decoded to get the current admin
    :type token: str
    :raises HTTPException: If the token is not valid
    :return: The current admin
    :rtype: Admin
    """
    try:
        payload = jwt.decode(token, Settings().dict()['secret_key'],
                             algorithms=[ALGORITHM])
        name = payload.get('name')
        if name is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The token is not valid.')
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='JWTError: the token cannot be decoded.') from exc
    admin = get_admin(name=name)
    if admin is None:
        if name is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The admin contained in the token is not valid.')
    return admin
