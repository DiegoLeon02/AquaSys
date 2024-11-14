from django import forms
from .models import Reporte

class ReporteFiltroForm(forms.Form):
    start_date = forms.DateField(required=True, label="Fecha de Inicio")
    end_date = forms.DateField(required=True, label="Fecha de Fin")
    type = forms.ChoiceField(choices=[('todos', 'Todos')] + Reporte.TIPOS_REPORTE, required=False, label="Tipo de Reporte")
