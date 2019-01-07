Pratica de programación integrativa: Feeling2songs

Para descargar la imágen:
docker pull carlosmanoso/feeling

Posteriomente ejecutaremos el contenedor en modo iterativo con este comando:
docker run -i -p 8000:8000 feeling python3 mane.py runserver 0.0.0.0:8000

Index:
http://localhost:8000/image2songs

Ahí podemos probar que la gestión de usuarios funciona y la captura de imagenes mediante webcam está en desarrollo.

Para probar la creación de listas tendremos que dirigirnos a:
http://localhost:8000/image2songs/upload

Donde pegaremos el link de una imagen y pulsaremos subir. Ahora debido a un problema con la librería, es por esto que tenemos que ejecutar el contenedor en modo iterativo, nos aparecerá un enlace en la terminal que sirve para capturar el token de Spotiy que tendremos que abrir.
Se abrirá una nueva pestaña y tendremos que copiar la URL completa en la terminal.
Posteriormente se creará en nuestro Spotify una playlist llamada Feeling Song y la fecha con 25 canciones basadas en nuestros gustos y las emociones de la imagen que hemos subido.
Atención: Debido a que la playlist se crea usando nuestros artistas escuchados es necesario que la cuenta de Spotify tenga algunas reproducciones de canciones.

Problemas:
Faces: Algunas veces la API de Face++ nos ha fallado por demasiadas peticiones, aunque se supone que son 1 petición por segundo, se produce un error de obtención del parámetro faces.