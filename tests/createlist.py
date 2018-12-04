import spotipy
import spotipy.util as util
import datetime

# Credenciales de la API
client_id = '86c70d9849ba4ba3b8c1a0d7590308d2'
client_secret = 'e3824d7c0cb94205ac4bb0d575f61306'


# Obtención del token
desired_scope = 'user-top-read'
uri = 'http://google.com/'  # Esta dirección es al a que se redirige después de aceptar el Token.
# cache_path = '/path/donde/se/guardan/las/credenciales'
token = util.prompt_for_user_token(username='username',
                                   scope=desired_scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=uri,
                                   # cache_path = ruta donde se guardan las credenciales,
                                   )
sp = spotipy.Spotify(auth=token)

usuario = sp.current_user()  # Se obtiene el nombre de usuario.
user = usuario['id']

# Emociones inventadas, esto tendría que venir del Face++
happiness = 0.039
anger = 0.001
neutral = 5.233
sadness = 0.001
fear = 0.001
surprise = 94.723
disgust = 0.001

# Emociones recibidas
danceability = happiness
energy = anger
instrumentalness = neutral
liveness = sadness
loudness = (fear*-1)
speechiness = surprise
valence = (disgust*-1)

# Crear playlist, crea una playlist con el timestamp para que no se llamen todas igual aunque no habría problema
ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nombreplaylist = ('Feeling song '+ts)
print(nombreplaylist)
playlist = sp.user_playlist_create(user, nombreplaylist, public=False)

# Añadir canciones a la playlist, obtiene los artistas más escuchados y después uno a uno busca recomendaciones con
# los objetivos de emociones que hemos especificado más arriba, luego los añade a la playlist.
artists = sp.current_user_top_artists(time_range='medium_term', limit=5)
for i, item in enumerate(artists['items']):
    print(i, item['name'])
    recommendations = sp.recommendations(seed_artists=[item['id']], limit=5,
                                         target_danceability=danceability,
                                         target_energy=energy,
                                         target_instrumentalness=instrumentalness,
                                         target_liveness=liveness,
                                         target_loudness=loudness,
                                         target_speechiness=speechiness,
                                         target_valence=valence)
    for song in recommendations['tracks']:
        print(song['name'], '-', song['artists'][0]['name'])
        add = sp.user_playlist_add_tracks(user, playlist['id'], [song['id']])
