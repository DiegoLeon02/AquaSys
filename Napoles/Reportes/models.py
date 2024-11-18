from django.db import models
from django.utils import timezone
from Embarques.models import Embarque  
from Administrador.models import LoginActivity
  
class LoginActivity(models.Model):
    usuario = models.CharField(max_length=100)  
    timestamp = models.DateTimeField(default=timezone.now)
    exitoso = models.BooleanField()  
    mensaje = models.TextField(null=True, blank=True)  

    def __str__(self):
        status = "Exitoso" if self.exitoso else "Fallido"
        return f"{self.usuario} - {status} - {self.timestamp}"

class Reporte(models.Model):
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100)  
    actividad = models.ForeignKey(
        LoginActivity, 
        on_delete=models.CASCADE, 
        related_name="login_reportes",  
        null=True, 
        blank=True
    )
    embarque = models.ForeignKey(
        Embarque, 
        on_delete=models.CASCADE, 
        related_name="embarque_reportes",  
        null=True, 
        blank=True
    )
    descripcion = models.TextField()  

    def __str__(self):
        return f"Reporte de Actividad - {self.usuario} - {self.fecha_generacion}"




