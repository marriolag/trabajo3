from django import forms

from . import models
from .models import Usuario, BusquedaUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"
    
class ArtistaForm(forms.ModelForm):
    class Meta:
        model = models.Artista
        fields = "__all__"
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"
        
        

class BusquedaUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.BusquedaUsuario
        fields = ('nombre_busqueda',)