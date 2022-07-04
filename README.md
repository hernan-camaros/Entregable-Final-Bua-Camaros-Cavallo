# djangocoder

Hola! Para este proyecto hemos decidido hacer una pagina web de Claudio Cavallo Carbonell (fotografo profesional) para inscribirse a cursos de fotografia. En principio para poder hacerlo correr, debemos instalar django. Para eso desde la terminal de visual ingresaremos el siguiente comando:


>>> python -m pip install django


Una vez instalado django, debemos abrir la carpeta en Visual Studio Code(VSC). Para eso abrimos el VSC y elegimos abrir la carpeta principal. En este caso la carpeta sera Entregable-Final-Bua-Camaros-Cavallo\ProyectoFinal.

Seguido de esto y parados sobre esa carpeta debemos ingresar el siguiente comando en la terminal:

>>> python manage.py 


Hecho esto y teniendo el proyecto abierto, hay que migrar los datos del proyecto al servidor y aplicar los cambios que queramos en la base de datos.

Para esto, debemos ejecutar el siguiente comando desde la terminal:


>>> python manage.py makemigrations


Ingresado este comando si no hay ningun error, el proximo comando a ingresar en la terminal sera el siguiente:


>>> python manage.py migrate



Excelente! ya tenemos migrados los datos a la base de datos. Lo unico que queda es iniciar el servidor. Para poder hacerlo, debemos ir a la terminal e ingresar el siguiente comando:


>>> python manage.py runserver

A la direccion de IP arrojada por la terminal, debemos pararnos encima del link, y clickear manteniendo la tecla CTRL para que el servidor se abra en una ventana de navegador.

Habiendo hecho esto, ingresaremos el nombre del url para poder ir a la pagina de inicio. El mismo es el siguiente: http://127.0.0.1:8000/CCC/
Desde alli, podremos ver tanto la informacion que provee la pagina sobre la persona que dicta las clases, como los tipos de cursos y sus respectivos formularios de inscripcion.

Por ultimo en caso de querer administrar la informacion ingresada debemos crear un superuser. Esto nos permitira agregar informacion a la base de datos creada. Para eso ingresaremos el siguiente comando


>>> python manage.py createsuperuser

Eligiremos un nombre de usuario, posteriormente una direccion de mail y una contraseña.

Luego Correremos otra vez el servidor con el comando ya anteriormente especificado.
>>> python manage.py runserver

Si todo este proceso esta bien ejecutado, estamos en codiciones de ingresar al panel de administracion. Para eso ingresaremos al url seguido de '/admin' con el nombre de usuario y contraseña que creamos previamente.

Desde ahi, podemos ingresar manualmente datos en la Base de Datos del servidor, especificando a que tipo de curso quiere inscribirse.



