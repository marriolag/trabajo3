from django import forms

from . import models

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
        
        