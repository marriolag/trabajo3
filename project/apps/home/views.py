from django.shortcuts import render
from . import forms
from .models import Usuario
# Create your views here.
def index(request):
    return render(request, "home/index.html",)

def crear_usuario(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.UsuarioForm()
    return render(request, "home/crear_usuario.html", {"form": form})

def crear_artista(request):
    if request.method == "POST":
        form = forms.ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:    
        form = forms.ArtistaForm()
    return render(request, "home/crear_artista.html", {"form": form})

def crear_album(request):
    if request.method == "POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.AlbumForm()
    return render(request, "home/crear_album.html",{"form": form})

def buscar_usuario(request):
    if request.method == 'POST':
        form = forms.BusquedaUsuarioForm(request.POST)
        if form.is_valid():
            nombre_busqueda = form.cleaned_data['nombre_busqueda']
            usuarios = Usuario.objects.filter(nombre__icontains=nombre_busqueda)
            return render(request, 'home/buscar_usuario.html', {'form': form, 'usuarios': usuarios})
    else:
        form = forms.BusquedaUsuarioForm()
    
    return render(request, 'home/buscar_usuario.html', {'form': form})
