import spotipy.util as util
# Este script genera un archivo .cache-username donde se almacena el token.
# Abre una pestaña en el navegador para que te autentifiques.
# Si ya contiene el token no hace nada.

# Credenciales de la API
client_id = '86c70d9849ba4ba3b8c1a0d7590308d2'
client_secret = 'e3824d7c0cb94205ac4bb0d575f61306'

user = 'user'
desired_scope = 'user-top-read playlist-modify-private playlist-read-collaborative playlist-modify-public ' \
                'playlist-read-private '
uri = 'http://google.com/'  # Esta dirección es al a que se redirige después de aceptar el Token.
# cache_path = '/path/donde/se/guardan/las/credenciales'
token = util.prompt_for_user_token(username=user,
                                   scope=desired_scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=uri,
                                   # cache_path = ruta donde se guardan las credenciales,
                                   )
