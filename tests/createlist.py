import spotipy
import spotipy.util as util

# Credenciales de la API
client_id = '86c70d9849ba4ba3b8c1a0d7590308d2'
client_secret = 'e3824d7c0cb94205ac4bb0d575f61306'

user = 'username'
desired_scope = 'user-top-read'
uri = 'http://google.com/'  # Esta dirección es al a que se redirige después de aceptar el Token.
# cache_path = '/path/donde/se/guardan/las/credenciales'
token = util.prompt_for_user_token(username=user,
                                   scope=desired_scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=uri,
                                   # cache_path = ruta donde se guardan las credenciales,
                                   )

sp = spotipy.Spotify(auth=token)
ranges = ['short_term', 'medium_term', 'long_term'] # Top artistas a corto medio y largo plazo
for range in ranges:
    print("range:", range)
    results = sp.current_user_top_artists(time_range=range, limit=5)
    for i, item in enumerate(results['items']):
        print(i, item['name'])
print()
