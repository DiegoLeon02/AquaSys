from django.db import models

# Modelo para Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    residencia = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.posicion}"