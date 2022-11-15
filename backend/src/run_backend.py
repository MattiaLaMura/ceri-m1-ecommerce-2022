""" This file contains all the **Backend routes**. """
import datetime
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.backend_metadata import DESCRIPTION, TAGS_METADATA
from src.classes.artist import get_all_artists
from src.classes.album import get_albums_from_artist
from src.classes.song import get_songs_from_album
from src.database.database import Database

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


@app.get('/add/artist', tags=['Add Artist'], status_code=status.HTTP_200_OK)
def add_artist(artist_name: str, is_active: bool):
    """ This route adds a new artist in the database. """
    my_database = Database()
    my_database.add_artist(artist_name, is_active)
    my_database.close()
    return {'message': 'A new artist has been added to the database.'}


@app.get('/add/album', tags=['Add Album'], status_code=status.HTTP_200_OK)
def add_album(artist_id: int, album_title: str, album_year: datetime.date, album_cover: str):
    """ This route adds a new album in the database. """
    my_database = Database()
    my_database.add_album(artist_id, album_title, album_year, album_cover)
    my_database.close()
    return {'message': 'A new album has been added to the database.'}


@app.get('/add/song', tags=['Add Song'], status_code=status.HTTP_200_OK)
def add_song(album_id: int, song_title: str, song_length: int):
    """ This route adds a new song in the database. """
    my_database = Database()
    my_database.add_song(album_id, song_title, song_length)
    my_database.close()
    return {'message': 'A new song has been added to the database.'}


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


@app.get('/get/songs', tags=['Get Songs'], status_code=status.HTTP_200_OK)
def get_songs(album_id: int):
    """ This route gets all the songs of an album from the database. """
    try:
        songs = get_songs_from_album(album_id)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(exc)) from exc
    return {'songs': songs}
