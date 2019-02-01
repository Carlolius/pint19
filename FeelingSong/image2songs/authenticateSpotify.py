from spotipy import oauth2


def gettoken(request):
    username = str(request.user)
    client_id = '86c70d9849ba4ba3b8c1a0d7590308d2'
    client_secret = 'e3824d7c0cb94205ac4bb0d575f61306'
    scope = 'user-top-read playlist-modify-private playlist-read-collaborative playlist-modify-public playlist-read-private '
    redirect_uri = 'http://localhost:8000/image2songs/callback'  # Esta dirección es al a que se redirige después de aceptar el Token.
    cache_path = ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, cache_path=cache_path)
    return sp_oauth


def authenticate(request):
    sp_oauth = gettoken(request)
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        try:
            import webbrowser
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except:
            print("no se abrio el navegador")


def savetoken(request, url):
    sp_oauth = gettoken(request)
    code = sp_oauth.parse_response_code(url)
    token_info = sp_oauth.get_access_token(code)
    print(token_info)
    return token_info
