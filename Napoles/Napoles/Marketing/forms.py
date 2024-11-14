from django import forms
from .models import EncuestaSatisfaccion, PublicacionRedesSociales, CampaniaPublicitaria

class EncuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = EncuestaSatisfaccion
        fields = ['cliente', 'respuestas']

class PublicacionRedesSocialesForm(forms.ModelForm):
    class Meta:
        model = PublicacionRedesSociales
        fields = ['contenido', 'fecha_programada', 'plataforma']

class CampaniaPublicitariaForm(forms.ModelForm):
    class Meta:
        model = CampaniaPublicitaria
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'presupuesto', 'resultado']
