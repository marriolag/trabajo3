from django.db import models

# Creacion de los modelos
class Usuario(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=8)
    nacionalidad = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.apellido
        #return "Apellido y Nombre: " + self.apellido,self.nombre + " - Cedula: " + str(self.cedula)
        
class Artista(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30)
    
    def __str__(self):
        return self.apellido
        #return "Apellido y Nombre: " + self.apellido, self.nombre

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_lanzamiento = models.DateField()
    estilo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
        #return "Nombre: " +self.nombre + "Estilo de Musica: " +self.estilo


class BusquedaUsuario(models.Model):
    nombre_busqueda = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_busqueda