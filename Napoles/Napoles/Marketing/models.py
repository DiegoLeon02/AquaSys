from django.db import models

class EncuestaSatisfaccion(models.Model):
    cliente = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    respuestas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Encuesta para {self.cliente} - {self.fecha_envio.strftime('%d-%m-%Y')}"

class PublicacionRedesSociales(models.Model):
    contenido = models.TextField()
    fecha_programada = models.DateTimeField()
    plataforma = models.CharField(max_length=50, choices=[
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn')
    ])

    def __str__(self):
        return f"Publicación en {self.plataforma} programada para {self.fecha_programada.strftime('%d-%m-%Y %H:%M')}"

class CampaniaPublicitaria(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Campaña {self.nombre} - {self.fecha_inicio.strftime('%d-%m-%Y')}"
