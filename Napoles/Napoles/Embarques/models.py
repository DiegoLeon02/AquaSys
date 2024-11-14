from django.db import models

# Create your models here.
from django.db import models

class Embarque(models.Model):
    numero_embarque = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=100)
    exportador = models.CharField(max_length=200)
    importador = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.numero_embarque} - {self.estado}"
