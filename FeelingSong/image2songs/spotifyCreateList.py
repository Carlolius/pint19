import spotipy
import spotipy.util as util
import datetime
from .obtainFeelings import obtainFeelings
from .authenticateSpotify import gettoken
from spotipy import oauth2


def createlist(request, imagen):
    sp_oauth = gettoken(request)

    token = sp_oauth.get_cached_token()
    if token:
        sp = spotipy.Spotify(auth=token)
        # Se obtiene el usuario.
        user = (sp.current_user())['id']

        # Obtenemos los feelings pasados en la foto de obtainFeelings
        decodedFeelings = obtainFeelings(imagen)

        # Asignación Json->Spotify
        danceability = decodedFeelings['faces'][0]['attributes']['emotion']['happiness']
        energy = decodedFeelings['faces'][0]['attributes']['emotion']['anger']
        instrumentalness = decodedFeelings['faces'][0]['attributes']['emotion']['neutral']
        liveness = decodedFeelings['faces'][0]['attributes']['emotion']['sadness']
        loudness = (decodedFeelings['faces'][0]['attributes']['emotion']['fear'])*-1
        speechiness = decodedFeelings['faces'][0]['attributes']['emotion']['surprise']
        valence = (decodedFeelings['faces'][0]['attributes']['emotion']['disgust'])*-1

        # Crear playlist, crea una playlist con el timestamp para que no se llamen todas igual aunque no habría problema
        ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        nombreplaylist = ('Feeling song '+ts)
        #  print(nombreplaylist)
        playlist = sp.user_playlist_create(user, nombreplaylist, public=False)

        # Añadir canciones a la playlist, obtiene los artistas más escuchados y después uno a uno busca recomendaciones con
        # los objetivos de emociones que hemos especificado más arriba, luego los añade a la playlist.
        artists = sp.current_user_top_artists(time_range='medium_term', limit=5)
        for i, item in enumerate(artists['items']):
            #  print(i, item['name'])
            recommendations = sp.recommendations(seed_artists=[item['id']], limit=5,
                                                 target_danceability=danceability,
                                                 target_energy=energy,
                                                 target_instrumentalness=instrumentalness,
                                                 target_liveness=liveness,
                                                 target_loudness=loudness,
                                                 target_speechiness=speechiness,
                                                 target_valence=valence)
            for song in recommendations['tracks']:
                #  print(song['name'], '-', song['artists'][0]['name'])
                add = sp.user_playlist_add_tracks(user, playlist['id'], [song['id']])
        return None
