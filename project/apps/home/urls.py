from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("crear_usuario/", views.crear_usuario, name="crear_usuario"),
    path("crear_artista/", views.crear_artista, name="crear_artista"),
    path("crear_album/", views.crear_album, name="crear_album"),
    path('buscar_usuario/', views.buscar_usuario, name="buscar_usuario"),
]
