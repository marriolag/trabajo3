from django.contrib import admin
from . import models

# Registro los modelos.

admin.site.register(models.Usuario)
admin.site.register(models.Artista)
admin.site.register(models.Album)
admin.site.register(models.BusquedaUsuario)