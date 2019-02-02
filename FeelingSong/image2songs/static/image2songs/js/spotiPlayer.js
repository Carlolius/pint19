window.onload = function() {
    var url=document.URL.split("?=")
    console.log(url[1]);
    newurl="https://open.spotify.com/embed/playlist/"+url[1];
    document.getElementById('spotiPlayer').src=newurl;
}
//Spliteamos el string para cambiar el src de nuestro widget y que así coincida con la playlist que acabamos de crear.