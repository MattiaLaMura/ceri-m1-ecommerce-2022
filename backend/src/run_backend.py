""" This file contains all the Backend routes. """
import datetime
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from globals import TOKEN_EXPIRE_MINUTES
from src.backend_metadata import DESCRIPTION, TAGS_METADATA
from src.classes.artist import get_all_artists
from src.classes.album import get_albums_from_artist, get_album_from_id, delete_album
from src.classes.song import get_songs_from_album
from src.classes.item import create_item, get_items, buy_item, delete_item, update_item
from src.classes.token import Token, create_access_token, get_current_user, \
    get_current_admin
from src.classes.admin import Admin, create_admin, authentication as admin_authentication
from src.classes.user import authentication, get_password_hash, \
    verify_email, get_users, create_user, User
from src.database.database import Database
from src.classes.algolia import index_catalog, search_engine

# Initialize the API
app = FastAPI(title='Jean Cloud Vinyl Backend',
              description=DESCRIPTION,
              openapi_tags=TAGS_METADATA)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', tags=['Health Check'], status_code=status.HTTP_200_OK)
def health_check():
    """ This route checks if the Backend is running. """
    return {'message': 'Jean Cloud Vinyl Backend is running.'}


@app.get('/create/database', tags=['Create Database'], status_code=status.HTTP_200_OK)
def create_database():
    """ This route creates the Backend database. """
    my_database = Database()
    my_database.create_tables()
    my_database.close()
    return {'message': 'The database has been created.'}


@app.post('/signup', tags=['Sign Up'], status_code=status.HTTP_200_OK)
def sign_up(user_name: str, user_email: str, user_password: str):
    """ This route creates and add a new user in the database. """
    if not verify_email(user_email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The email is not valid or it has already been taken.')
    password = get_password_hash(user_password)
    create_user(user_name, user_email, password)
    return {'message': 'The user has been created.'}


@app.post('/add/admin', tags=['Add Admin'], status_code=status.HTTP_200_OK)
def add_admin(admin_name: str, admin_password: str):
    """ This route creates and add a new admin in the database. """
    password = get_password_hash(admin_password)
    create_admin(admin_name, password)
    return {'message': 'The admin has been created.'}


@app.post('/token', tags=['Token'], response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """ This route takes an email, a password and it returns a token. """
    user = authentication(form_data.username, form_data.password)
    if user:
        token = create_access_token(data={'email': user.user_email},
                                    expires_delta=datetime.timedelta(
                                        minutes=TOKEN_EXPIRE_MINUTES))
        return {'access_token': token, 'token_type': 'bearer'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='The email or password is incorrect.')


@app.post('/token_backoffice', tags=['Token BackOffice'], response_model=Token)
async def login_for_access_token_2(form_data: OAuth2PasswordRequestForm = Depends()):
    """ This route takes a name, a password and it returns a token. """
    admin = admin_authentication(form_data.username, form_data.password)
    if admin:
        token = create_access_token(data={'name': admin.admin_name},
                                    expires_delta=datetime.timedelta(
                                        minutes=TOKEN_EXPIRE_MINUTES))
        return {'access_token': token, 'token_type': 'bearer'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='The name or password is incorrect.')


@app.get('/get/users', tags=['Get Users'], status_code=status.HTTP_200_OK)
def get_all_users(current_admin: Admin = Depends(get_current_admin)):
    """ This route gets all the users from the database. """
    print("Hello admin " + current_admin.admin_name)
    return {'users': get_users()}


@app.get('/get/current/user', tags=['Get Current User'], status_code=status.HTTP_200_OK)
def get_user_current(current_user: User = Depends(get_current_user)):
    """ This route gets all the information of the current user. """
    return {'current_user': current_user}


@app.get('/get/current/admin', tags=['Get Current Admin'], status_code=status.HTTP_200_OK)
def get_admin_current(current_admin: Admin = Depends(get_current_admin)):
    """ This route gets all the information of the current admin. """
    return {'current_admin': current_admin}


@app.get('/get/orders', tags=['Get Orders'], status_code=status.HTTP_200_OK)
def get_orders(user_id: int, current_admin: Admin = Depends(get_current_admin)):
    """ This route gets all the orders of an user from the database. """
    print("Hello admin " + current_admin.admin_name)
    orders = get_items(user_id)
    return {'orders': orders}


@app.get('/add/artist', tags=['Add Artist'], status_code=status.HTTP_200_OK)
def add_artist(artist_name: str, is_active: bool,
               current_admin: Admin = Depends(get_current_admin)):
    """ This route adds a new artist in the database. """
    print("Hello admin " + current_admin.admin_name)
    my_database = Database()
    my_database.add_artist(artist_name, is_active)
    my_database.close()
    return {'message': 'A new artist has been added to the database.'}


@app.get('/add/album', tags=['Add Album'], status_code=status.HTTP_200_OK)
def add_album(artist_id: int, album_title: str, album_year: datetime.date, album_cover: str,
              current_admin: Admin = Depends(get_current_admin)):
    """ This route adds a new album in the database. """
    print("Hello admin " + current_admin.admin_name)
    my_database = Database()
    my_database.add_album(artist_id, album_title, album_year, album_cover)
    my_database.close()
    return {'message': 'A new album has been added to the database.'}


@app.get('/add/song', tags=['Add Song'], status_code=status.HTTP_200_OK)
def add_song(album_id: int, song_title: str, song_length: int,
             current_admin: Admin = Depends(get_current_admin)):
    """ This route adds a new song in the database. """
    print("Hello admin " + current_admin.admin_name)
    my_database = Database()
    my_database.add_song(album_id, song_title, song_length)
    my_database.close()
    return {'message': 'A new song has been added to the database.'}


@app.get('/search_engine', tags=['Search Engine'], status_code=status.HTTP_200_OK)
def search(word_searched: str):
    """ This route uses the Algolia search engine. """
    index_catalog()
    return {'result': search_engine(word_searched)}


@app.get('/add/item', tags=['Add Item'], status_code=status.HTTP_200_OK)
def add_item(album_id: int, paid: bool, current_user: User = Depends(get_current_user)):
    """ This route adds a new item in the database. """
    create_item(album_id, current_user.user_id, paid)
    return {'message': 'A new item has been added to the database.'}


@app.get('/get/artists', tags=['Get Artists'], status_code=status.HTTP_200_OK)
def get_artists():
    """ This route gets all the artists from the database. """
    try:
        artists = get_all_artists()
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(exc)) from exc
    return {'artists': artists}


@app.get('/get/albums', tags=['Get Albums'], status_code=status.HTTP_200_OK)
def get_albums(artist_id: int):
    """ This route gets all the albums of an artist from the database. """
    try:
        albums = get_albums_from_artist(artist_id)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(exc)) from exc
    return {'albums': albums}


@app.get('/get/album', tags=['Get Album'], status_code=status.HTTP_200_OK)
def get_album(album_id: int):
    """ This route gets an album from the database. """
    try:
        album = get_album_from_id(album_id)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(exc)) from exc
    return {'album': album}


@app.get('/get/songs', tags=['Get Songs'], status_code=status.HTTP_200_OK)
def get_songs(album_id: int):
    """ This route gets all the songs of an album from the database. """
    try:
        songs = get_songs_from_album(album_id)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(exc)) from exc
    return {'songs': songs}


@app.get('/remove/album', tags=['Remove Album'], status_code=status.HTTP_200_OK)
def remove_album(album_id: int):
    """ This route allows the user to remove an album. """
    if delete_album(album_id):
        return {'message': 'The album has been removed.'}
    return {'message': 'The album cannot be removed.'}


@app.get('/get/items', tags=['Get Items'], status_code=status.HTTP_200_OK)
def get_all_items(current_user: User = Depends(get_current_user)):
    """ This route gets all the items of an user from the database. """
    items = get_items(current_user.user_id)
    return {'items': items}


@app.get('/buy/items', tags=['Buy Item'], status_code=status.HTTP_200_OK)
def pay_items(item_id: int, current_user: User = Depends(get_current_user)):
    """ This route allows the user to buy an item. """
    if buy_item(item_id, current_user.user_id):
        return {'message': 'The item has been bought.'}
    return {'message': 'The item cannot be bought.'}


@app.get('/remove/item', tags=['Remove Item'], status_code=status.HTTP_200_OK)
def remove_item(item_id: int, current_user: User = Depends(get_current_user)):
    """ This route allows the user to remove an item. """
    if delete_item(item_id, current_user.user_id):
        return {'message': 'The item has been removed.'}
    return {'message': 'The item cannot be removed.'}


@app.get('/update/item', tags=['Update Item'], status_code=status.HTTP_200_OK)
def update_status_item(item_id: int, user_id: int, item_status: str,
                       current_admin: Admin = Depends(get_current_admin)):
    """ This route allows the admin to update an item. """
    print("Hello admin " + current_admin.admin_name)
    if update_item(item_id, user_id, item_status):
        return {'message': 'The item has been updated.'}
    return {'message': 'The item did not change.'}
