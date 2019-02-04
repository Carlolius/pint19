Pratica de programación integrativa: Feeling2songs

Para descargar la imágen:
docker pull carlosmanoso/feeling

Posteriomente ejecutaremos el contenedor en modo con este comando:
docker run -p 8000:8000 feeling python3 manage.py runserver 0.0.0.0:8000

Index:
http://localhost:8000/image2songs

Esta práctica genera una playlist en Spotify cruzando las APIS de Face++ y Spotify, dicha playlist se genera dependiendo de las emociones reconocidas por Face++, para ello hay que proporcionar una imágen, ya sea tomándola con la webcam, pasándo una URL o directamente subiéndola.
Tras crear una playlist podemos reproducir el contenido de la misma desde un widget de Spotify en nuestra página web, para escuchar más de 30 segundos de cada canción necesitaremos una cuenta de Spotify premium.
Cada playlist es generada con 25 canciones con las recomendaciones de los 5 artistas escuchados a medio termino.
La aplicación tiene soporte multiusuario y necesitas tener escuchada música en tu cuenta de Spotify.

Errores conocidos:

-La petición entre APIS tarda un poco en procesarse.
-La gráfica de los historiales puede ser un poco confusa cuando hay pocas imágenes.
-Por falta de tiempo no se ha podido implementar cambiar la imágen de perfil.
-La imágen capturada con la webcam se descarga al ordenador del usuario, no va directamente al servidor.