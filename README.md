#Tercera Entrega PYTHON: 

Aquí tienes una guía general para desarrollar un proyecto web Django utilizando el patrón MVT (Modelo-Vista-Plantilla), que incluye herencia de HTML, clases en el modelo y formularios para insertar datos.

Sigue estos pasos para crear el proyecto:

Configuración inicial:

Si no tienes Python instalado, descárgalo e instálalo en tu sistema.
Utiliza el administrador de paquetes pip para instalar Django ejecutando el siguiente comando en la terminal: pip install django.
Crea un nuevo proyecto Django ejecutando el siguiente comando en la terminal: django-admin startproject proyecto.
Define el modelo:

Abre el archivo models.py en la carpeta del proyecto y define las clases de modelo necesarias.
Si deseas implementar herencia en tus clases de modelo, utiliza la herencia de modelos proporcionada por Django.
Crea las vistas:

Abre el archivo views.py en la carpeta de la aplicación y define las vistas para manejar las solicitudes del usuario.
Las vistas pueden renderizar plantillas HTML, procesar formularios y realizar operaciones en el modelo.
Configura las URLs:

Crea un archivo urls.py en la carpeta de la aplicación y define las URLs que corresponden a cada vista.
Configura las URLs del proyecto principal para incluir las URLs de la aplicación.
Crea las plantillas HTML:

Crea una carpeta llamada templates en la carpeta de la aplicación.
Crea plantillas HTML para cada vista y utiliza la herencia de plantillas para evitar la duplicación de código HTML.
Define los formularios:

Crea un archivo forms.py en la carpeta de la aplicación y define los formularios necesarios para insertar datos en el modelo.
Utiliza las clases de formulario proporcionadas por Django para facilitar la validación y el procesamiento de los datos del formulario.
Ejecuta el servidor de desarrollo:

Abre una terminal, navega hasta la carpeta del proyecto y ejecuta el comando python manage.py runserver.
Accede al servidor de desarrollo en tu navegador para probar y verificar las funcionalidades de tu aplicación web.