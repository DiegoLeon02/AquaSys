from django import forms
from .models import Embarque

class EmbarqueForm(forms.ModelForm):
    class Meta:
        model = Embarque
        fields = ['numero_embarque', 'estado', 'exportador', 'importador']
