from django.db import models


# Modelos aquí 

from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver

class Perfil(models.Model):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Gerente', 'Gerente'),
    ]

    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.rol}"