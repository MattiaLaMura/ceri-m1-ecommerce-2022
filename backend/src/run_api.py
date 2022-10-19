""" This file contains all the **Backend routes**. """
from fastapi import FastAPI, status, HTTPException
from api_metatdata import DESCRIPTION, TAGS_METADATA
from classes.artist import get_all_artists
from classes.album import get_albums_from_artist
from classes.song import get_songs_from_album

# Initialize the API
app = FastAPI(title='Jean Cloud Vinil API', description=DESCRIPTION, openapi_tags=TAGS_METADATA)


@app.get('/', tags=['Health Check'], status_code=status.HTTP_200_OK)
def health_check():
    """ This route checks if the Backend is running. """
    return {'message': 'Jean Cloud Vinil API is running.'}


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
