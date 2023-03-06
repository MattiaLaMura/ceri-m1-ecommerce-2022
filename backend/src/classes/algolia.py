from algoliasearch.search_client import SearchClient
from environment_variable import Settings
from src.classes.artist import get_all_artists
from src.classes.album import get_albums_from_artist
from src.classes.song import get_songs_from_album


def get_vars():
    client = SearchClient.create(Settings().dict()['algolia_application_id'],
                                Settings().dict()['algolia_api_key'])
    index = client.init_index(Settings().dict()['algolia_index_name'])
    return index


def index_catalog():
    """ This method uses Algolia to index the catalog. """
    index = get_vars()
    artists = get_all_artists()
    for artist in artists:
        albums = get_albums_from_artist(artist.artist_id)
        for album in albums:
            songs = get_songs_from_album(album.album_id)
            catalog_object = {'artist_name': artist.artist_name, 'album_title': album.album_title,
                              'objectID': album.album_id}
            catalog_object['Songs'] = ' '.join(
                [song.song_title for song in songs])
            try:
                # Try to retrieve the object from the index
                index.get_object(catalog_object['objectID'])
                # If the object was found, update it
                index.update_object(catalog_object)
            except Exception:
                # If the object was not found, add it
                index.save_object(catalog_object)


def search_engine(word_searched: str):
    """ This method uses Algolia to provide a search engine. """
    index = get_vars()
    return index.search(word_searched, {"hitsPerPage": 5})
