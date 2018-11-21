import os
import spotipy.util as util
# Este script genera un archivo .cache-username donde se almacena el token. Abre una pestaña en el navegador para que te autentifiques.
# Si ya contiene el token no hace nada.
# credentials
user = 'username'
desired_scope = 'playlist-modify-private'
id = os.environ.get('SPOT_CLIENT')
secret = os.environ.get('SPOT_SECRET')
uri = 'http://google.com' # Esta dirección es al a que se redirige después de aceptar el Token.
token = util.prompt_for_user_token(username=user,
                                   scope=desired_scope,
                                   client_id=id,
                                   client_secret=secret,
                                   redirect_uri=uri)
