from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%d-%m-%Y %H:%M')}"
