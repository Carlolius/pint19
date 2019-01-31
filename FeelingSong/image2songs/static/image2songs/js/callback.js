window.onload=function(){
    var spotifyAccessToken = "http://localhost:8000/" + parseHash(String(window.location.hash));
    window.print (spotifyAccessToken);
    window.print ("se ha podido imrprimir");
    $.ajax({
        method: 'POST',
        url: 'token/',
        data: spotifyAccessToken,
    });
    window.close();
}