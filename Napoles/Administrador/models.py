from django.db import models
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
# Modelos aquí 

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


class LoginActivity(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="perfiles")  
    timestamp = models.DateTimeField(default=timezone.now) 
    exitoso = models.BooleanField()  
    mensaje = models.TextField(null=True, blank=True)  

    def __str__(self):
        status = "Exitoso" if self.exitoso else "Fallido"
        return f"{self.perfil.nombre} - {status} - {self.timestamp}"

