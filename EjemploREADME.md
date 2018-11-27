Este tutorial es una versión reducida del tutorial de Django contenido en la
[página del proyecto](https://docs.djangoproject.com/en/1.11/intro/tutorial01/). Se recomienda a los alumnos seguir el tutorial paso a paso
y desde el principio. De hecho, para que el alumno pueda tener varios ejemplos
paso a paso de uso de Django, la página web que implementa el presente tutorial
es distinta a la implementada en el tutorial original. **El presente tutorial ha sido
desarrollado utilizando la versión 1.11.7 de Django y la versión 3.6 de Python.** Es posible que haya pequeños
problemas en su desarrollo utilizando versiones distintas.

# Índice del tutorial
1. [Configurando el entorno e iniciando el proyecto](#configurando-el-entorno-e-iniciando-el-proyecto)
2. [Configurando un gestor de base de datos](#configurando-un-gestor-de-base-de-datos)
3. [Creando nuestra primera app](#creando-nuestra-primera-app)
4. [Creando la zona admin](#creando-la-zona-admin)
4. [Creando nuestras primeras vistas](#creando-nuestras-primeras-vistas)
5. [Mejorando nuestras vistas](#mejorando-nuestras-vistas)
6. [Usando plantillas](#usando-plantillas)
7. [Usando formularios](#usando-formularios)
8. [Usando usuarios] (#usando-usuarios )
9. [Integrando con APIs de terceros] (#integrando-con-apis-de-terceros )

---
### Configurando el entorno e iniciando el proyecto

Asumiendo que ya tenemos instalado Python3 en nuestro equipo, debemos asegurarnos de instalar la última versión disponible de Django ejecutando el comando

```
sudo pip install django
```

Comprobaremos qué versió de Django tenemos instalada ejecutando el comando

```
python3 -m django --version
```

En este punto tendrás que clonar el Paso 0 de este repositorio para empezar a trabajar

```
git clone https://github.com/diegoandradecanosa/pintDjango 
cd pintDjango
git checkout Paso0
```
Ahora, dentro del directorio del repositorio (pintDjango) vamos a crear el repositorio

```
django-admin startproject myciao
```

Este comando creará el proyecto y lo inicializará con una serie de ficheros básicos. Comprúebalo ejecutando el comando

```
ls -R myciao
```

Cuya salida debería ser algo similar a esto

``` 
myciao/:
manage.py  myciao

myciao/myciao:
__init__.py  settings.py  urls.py  wsgi.py
```

Ahora entramos en el proyecto y arrancamos el servidor de desarrollo

```
cd myciao
python3 manage.py runserver
```
Si el servidor se arranca por defecto, deberíamos poder visitar una página por defecto en [http://127.0.0.1:8000/
](http://127.0.0.1:8000/)

---
### Configurando un gestor de base de datos

Ahora deberíamos configurar un gesto de base de datos. Uno de los más básicos que podemos utilizar es sqlite. Antes de configurarlo deberemos instalarlo en nuestro sistema. El método para instalarlo dependerá del sistema operativo que tengamos. Por ejemplo, en Ubuntu Linux esto se hace con el comando

```
sudo apt-get install sqlite
```

En sqlite la base de datos está almacenada en un fichero, y el nombre y la ruta de dicho fichero es toda la configuración que tenemos que proporcionar a Django. En myciao/setting.py ya tenemos una configuracin por defecto que ya podemos dejar tal y como está

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Además, aprovecharemos para hacer algunos ajustes sobre el idioma y la zona horaria en este mismo fichero

```
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
```
En este punto, también es interesante fijarnos en otros aspectos de la configuración por defecto como por ejemplo la variable INSTALLED_APPS que contiene una lista de todas las apps que serán instaladas por defecto. Algunos ejemplos son auth, que proporciona un sistema de autenticación básica de usuarios, o sessions, que da soporte al manejo de sesiones del navegador.

En este punto, y para inicializar nuestra base de datos con aquellas tablas que darán soporte a estas apps que vienen instaladas por defecto, deberemos ejecutar la siguiente secuencia de comandos

```
python3 manage.py makemigration
python3 manage.py migrate
```
Esta secuencia de comandos, muy popular entre los usuarios de Django, deberá ser ejecutada cada vez que hagamos un cambio en nuestro proyecto que implique un cambio en el esquema de la base de datos. El comando makemigrations prepara una serie de scripts que ejecutará estos cambios, y migrate ejecuta dichos scripts. 

Es conveniente en este punto crear un superusuario para el sistema de autenticación. Usaremos el comando.

```
python3 manage.py createsuperuser
```
---
### Creando nuestra primera app

Hemos visto que Django proporciona una serie de aplicaciones de uso común
que nos facilita la realización de tareas que son comunes a todas las páginas
web. Sin embargo, el verdadero interés de Django están en apoyarnos en dichas
aplicaciones para crear nuestras propias aplicaciones. En este ejemplo paso a
paso nos proponemos crear una simple página web que nos muestra una lista de
productos y una lista de opiniones asociadas a dichos productos. Posteriormente
extenderemos la aplicación para permitir a los usuarios de la misma añadir
nuevos productos o nuevas opiniones de un producto determinado a través de
un formulario.

A nuestra aplicación le vamos a llamar reviews y para crearla vamos a darle
un nuevo uso al script manage.py.

```
python3 manage.py starapp reviews
```

Es interesante examinar el listado de ficheros que Django incluye inicialmente en esta aplicación.

```
ls -R reviews
```
La salida debería ser algo como lo siguiente.

```
reviews/:
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py

reviews/migrations:
__init__.py
```

Para que nuestro proyecto sea consciente de la existencia de esta primera app tenemos que incluirla explícitamente en la lista asociada a la variable INSTALLED_APPS del fichero myciao/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews',
]
```

Ahora tenemos que crear el modelo de base de datos que dará soporte a esta nueva app. Tendremos 2 tablas Product y Review, que contendrán la informacin de los productos y de las opiniones sobre estos productos, y que por lo tanto estarán relacionadas entre si. Para actualizar este fichero deberás ejecutar el siguiente comando.

```
git checkout Paso1
```

Ahora podemos examinar el nuevo contenido del fichero models.py.

El ORM sabe que tiene que crear una tabla de la base de datos por cada clase y un
campo en dicha tabla por cada atributo que definamos dentro de dicha
clase. Si el usuario no especifica una clave primaria, como en el ejemplo, el
ORM asociará a dicha base de datos un identificador sintético autoincremental de nombre id. 
Como vemos a cada atributo se le asigna un
valor y dicho valor define el tipo de campo de la base de datos asociado a dicho
atributo. Es de especial interés el campo product dentro de clase Review que
establece la relación entre la clase Model y la clase Review. En [esta página del
manual de Django](https://docs.djangoproject.com/en/1.11/ref/models/fields/) tenéis una lista de los tipos de campos que se pueden definir.
También hemos definido un método unicode que será utilizado luego por
Django para visualizar el contenido de una instancia de una clase determinada.

Ahora sı́ tenemos cambios pendientes de realizar en el esquema de la ba-
se de datos, para realizarlos debemos ejecutar los siguientes comandos que ya
conocemos.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Una vez hecho esto vamos a ver al ORM en acción, veremos cómo nos facilita
la persistencia dentro de nuestra página web. Para ellos vamos a abrir un shell
que nos permite ver de forma iterativa el efecto de diferentes comandos. Para
abrirlo vamos a utilizar, otra vez, el script manage.py para abrir una sesión interactiva.

```
python3 manage.py shell
```

Dentro de la sesión podemos experimentar con la siguiente secuencia de comandos.

```
from reviews.models import Product, Review
Product.objects.all()
p=Product(barcode='AB1',name='TV Sony Bravia')
p.save()
p.id
p.name
p.barcode
p.barcode=’AB01’
p.save()
Product.objects.all()
p.review_set.create(title='Muy bueno',text='Me gusta mucho esta tv')
p.review_set.create(title='Muy malo',text='No me gusta nada esta tv')
p.review_set.all()
```
---
### Creando la zona admin

Si visitamos la siguiente dirección [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) podremos visitar la zona de administración creada por defecto por Django, utilizando el usuario y la contraseña de superusuario para este proyecto que habíamos configurado al principio de este tutorial.

En su estado por defecto esta zona de administración sólo nos permite realizar operaciones CRUD (create, read, update and delete) sobre los usuarios y los grupos del app de autenticación (auth). Si queremos por ejemplo dar acceso a las tablas Product y Review de nuestra nueva aplicación deberemos indicarlo exprésamente en el fichero reviews/admin.py Para actualizar dicho fichero debemos ejecutar el siguiente comando

```
git checkout Paso2
```

Ahora puedes examinar el nuevo contenido del fichero reviews/admin.py.
Si visitamos de nuevo la zona de administración  [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) podremos comprobar que ahora sí podemos hacer las operaciones CRUD sobre las tablas Product y Review.

---
### Creando nuestra primera vista

Hasta ahora hemos creado una aplicación reviews y la hemos dotado de
un modelo de datos y de un área de administración, sin embargo, todavı́a queda
hacer lo más importante que es permitir que los usuarios puedan acceder a la
página web para visualizar productos y opiniones y añadir sus propios productos
y opiniones. Para ello tenemos que empezar a crear vistas, que es otro de los
componentes fundamentales de Django. La creación de una primera vista que devuelva un "Hola Mundo" se realiza en 3 pasos:

* La definición del comportamiento de la vista en si en el fichero reviews/views.py

* Añadir a la lista urlpatterns definida  en el fichero reviews/urls.py una asociación entre una determinada url y la vista que acabamos de definir. De este modo establecemos que determinadas urls serán respondidas con la vista que hemos definido.

* El fichero reviews/urls.py es un fichero urls.py de segundo nivel, que se circunscribe al ámbito de la aplicación reviews. Pero, todavía tenemos que instruir al fichero myciao/urls.py principal del proyecto sobre cómo llegar a él. La forma de hacerlo es indicando en dicho fichero que urls con una determinada forma tienen que ser resueltas en el fichero reviews/urls.py

Recupera estos cambios del repositorio ejecutando el comando

```
git checkout Paso3
```
Ahora puedes inspeccionar el nuevo contenido de los ficheros reviews/views.py, reviews/urls.py y myciao/urls.py.
Como podrás comprobar hemos definido dos vistas: index y detail. Index muestra un simple "Hola Mundo" y detail muestra un "Hola Mundo id" donde id es un identifidor numérico que se pasa a través de la url. A dichas vistas se puede llegar a través de las urls: [http://localhost:8000/reviews/](http://localhost:8000/reviews/) y [http://localhost:8000/reviews/id/](http://localhost:8000/reviews/id/). En la segunda url debemos sustituir id por un número entero.

---
### Mejorando nuestras vistas

En este punto hemos sido capaces de crear un par de vistas y a una de ellas hemos
sido capaces de pasarle un parámetro a través de la url, no cual nos resultará de gran utilidad en el futuro. 
Nuestro siguiente objetivo es que las vistas hagan cosas útiles y para ello tenemos que acceder desde ella al modelo
de datos y generar código html.
En cuanto a la vista index nos gustarı́a que mostrase un listado de los
productos existentes en la base de datos y que el nombre de cada producto
fuese un enlace a la vista detail de ese producto. Por otra parte, la vista
detail nos gustarı́a que mostrase el nombre del producto y una lista de las
opiniones que tienen dicho producto. Para ello necesitamos carga una nueva versión del fichero reviews/views.py.

```
git checkout Paso4
```

Ahora podemos comprobar lo cambios en dicho fichero y el resulta que surte visitando [http://localhost:8000/reviews/](http://localhost:8000/reviews/)

---
### Usando plantillas

En nuestras vistas actuales aparece mezclado el código que utilizamos para acceder a los datos 
y el código html que formatea su aspecto lo cual resulta engorroso  poco práctico.
Afortunadamente Django nos permite desacoplar el código de la vista de el
código html que la de formato a través de un sistema de plantillas (templates).

En este paso del tutorial vamos a reescribir nuestras 2 vistas utilizando plantillas. 
Antes de hacerlo tenemos que crear un directorio donde poner nuestras plantillas.

```
mkdir -p reviews/templates/reviews/
```

Ejecutando el siguiente comando actualizamos los ficheros para este paso.

```
git checkout Paso5
```
Obtenemos 3 ficheros html para las plantillas: index.html, detail.html y base.html. Este último es un esqueleto que define el marco cuyo contenido luego se particulariza para cada plantilla concreta. A este mecanismo se le llama herencia de plantillas y si examinas esos 3 ficheros podrás entender fácilmente cómo funciona.

También obtenemos varios ficheros alojados en la carpeta reviews/static/reviews. Estos ficheros contienen hojas de estilo (css) y fichero javascript (js) que enriquecen el aspecto de la página web. El uso de ficheros estáticos como imágenes u hoja de estilo se realizar a través de una app que se llama staticfiles y que viene cargada por defecto. Poniendo los ficheros en un subdirectorio static dentro del directorio de mi app podremos acceder a ellos. Para ver un ejemplo de cómo referenciarlos inspecciona la plantilla base.html, donde aparecen varias referencias.

Finalmente el fichero views.py también ha sido actualizado. Ahora la información se recupera de la base de datos y se le pasa a la plantilla a través de un diccionario llamado contexto. La vista ejecuta la plantilla correspondiente pasándole como argumento dicho contexto y esta ejecución genera un html que se convierte en el resultado de la vista.

---
### Usando formularios

En este punto del tutorial queremos incorporar a la aplicacin 2 tipos de formularios: uno que nos permita añadir nuevos productos y otro que nos permita añadir nuevas reviews a un producto.

Para mejorar el aspecto de nuestros formularios y facilitar su creación vamos a utilizar un app de Django llamada django-crispy-forms [1]. Para instarla ejecutaremos el siguiente comando.

```
sudo pip3 install --upgrade django-crispy-forms
```
y añadir en el fichero settings.py a la variable INSTALLED_APPS la entrada cripsy_forms

```
INSTALLED_APPS = [
    ...
    'crispy_forms',
]
```
Ejecutando el siguiente comando actualizamos los ficheros para este paso.

```
git checkout Paso6
```

Los que vamos a recuperar es un nuevo fichero forms.py en el que vamos a encontrar la definición de los dos formularios que queremos añadir: añadir producto y añadir opinión. Una nueva versión de views.py donde las vistas correspondientes van a recibir los parámetros de dichos formularios y los van a añadir a la base de datos. Nuevas versiones de las templates, base.html, index.html y product_detail.html preparadas para mostrar los formularios correspondientes.

---
### Usando usuarios

En este punto del tutorial nos gustaría que la aplicación tenga usuarios y que ciertas funcionalidades de nuestra aplicación sólo las puedan utilizar ciertos tipos de usuarios, por ejemplo, no queremos que cualquier usuario pueda crear nuevos productos sólo aquellos que formen parte del staff (ver zona de administración)

Para ello nos vamos a utilizar el sistema de gestión de usuarios de django que ya viene habilitado a través de la app auth. Esta aplicación ya se encuentra habilitada por defecto en el fichero settings.py. Luego, con ayuda de los crispy-forms crearemos los correspondientes formulario de login y registro de usuarios, y una vista específica para hacer logout. Todos estos cambios estarán disponibles ejecutando el comando

```
git checkout Paso7
```
Inspecciona los cambios realizados en los ficheros forms.py, views.py, base.html, index.html, product_detail.html, e inspeccionar el contenido de la nueva template signup.html

---
### Integrando con APIs de terceros

En la vista de detalle de producto vamos a mostrar una lista de los 10 últimos tweets que contienen el nombre el producto. 
Los ficheros correspondientes a este paso se pueden actualizar ejecutando el siguiente comando.

```
git checkout Paso8
```
En views.py hay una función nueva que se llama getTweets y que recuperar estos 10 últimos tweets. En la vista detail estos tweets se pasan a la plantilla a través del contexto. Al final de la plantilla product_detail.html tenemos el código que recorrer la lista de tweets y los muestra.

[1] Django crispy forms https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms











































