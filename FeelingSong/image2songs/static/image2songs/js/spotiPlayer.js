window.onload = function() {
    var url=document.URL.split("?=")
    console.log(url[1]);
    newurl="https://open.spotify.com/embed/playlist/"+url[1];
    document.getElementById('spotiPlayer').src=newurl;
    newtweet="https://twitter.com/intent/tweet?source=webclient&text=Esta+es+tu+playlist+de+FeelingSong+"+newurl;
    document.getElementById('botontw').href=newtweet;
}
//Spliteamos el string para cambiar el src de nuestro widget y que así coincida con la playlist que acabamos de crear.