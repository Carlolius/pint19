import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials


def get_metadata(file_name, client_id = '86c70d9849ba4ba3b8c1a0d7590308d2', client_secret = 'e3824d7c0cb94205ac4bb0d575f61306'):

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    results = spotify.search(file_name, limit=1)

    results = results['tracks']['items'][0]  # Find top result
    album = results['album']['name']  # Parse json dictionary
    artist = results['album']['artists'][0]['name']
    song_title = results['name']
    album_art = results['album']['images'][0]['url']

    return artist, album, song_title, album_art

metadata=get_metadata('Queen')
print(metadata)