from algoliasearch.search_client import SearchClient
from environment_variable import Settings
from src.classes.artist import get_all_artists
from src.classes.album import get_all_albums
from src.classes.song import get_all_songs

client = SearchClient.create(Settings().dict()['algolia_application_id'],
                             Settings().dict()['algolia_api_key'])
index = client.init_index(Settings().dict()['algolia_index_name'])


def index_catalog():
    """ This method uses Algolia to index the catalog. """
    artists = get_all_artists()
    albums = get_all_albums()
    for artist in artists:
        try:
            # Try to retrieve the object from the index
            index.get_object(artist.artist_id)
            # If the object was found, update it
            index.update_object(artist)
        except algoliasearch.AlgoliaException:
            # If the object was not found, add it
            index.add_object(artist)
    for album in albums:
        try:
            index.get_object(album.album_id)
            index.update_object(album)
        except algoliasearch.AlgoliaException:
            index.add_object(album)


def search_engine(word_searched: str):
    """ This method uses Algolia to provide a search engine. """
    return index.search(word_searched, {"hitsPerPage": 5})
