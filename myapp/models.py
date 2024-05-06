from django.db import models

# Create your models here.

# Podemos crear nuestros modelos y los datos que tendran
# para crear tablas y columnas en las DB


class Project(models.Model):
    # Podemos definir el tipo de datos y sus propiedades
    name = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # podemos hacer referencia a otras clases
    # on_delete = models.CASCADE permite eliminar los registros que esten asociados
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
