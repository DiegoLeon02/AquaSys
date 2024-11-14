from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Reporte, LoginActivity
from Embarques.models import Embarque  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# Vista para listar todos los reportes de actividad y embarques
def lista_reportes(request):
    actividades = LoginActivity.objects.all().order_by('-timestamp')
    embarques = Embarque.objects.all()
    return render(request, 'reportes.html', {'actividades': actividades, 'embarques': embarques})

# Exportar el reporte de actividad de inicio de sesión en formato PDF
def exportar_pdf_login_activity(request, actividad_id):
    actividad = get_object_or_404(LoginActivity, pk=actividad_id)
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Detalles del intento de inicio de sesión
    c.drawString(100, 750, f"Reporte de Inicio de Sesión - ID: {actividad.id}")
    c.drawString(100, 730, f"Usuario: {actividad.usuario}")
    c.drawString(100, 710, f"Fecha y Hora: {actividad.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 690, f"Resultado: {'Exitoso' if actividad.exitoso else 'Fallido'}")
    if actividad.mensaje:
        c.drawString(100, 670, f"Mensaje: {actividad.mensaje}")
    c.showPage()
    c.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_login_{actividad.id}.pdf"'
    return response

# Exportar el reporte de embarque en formato PDF
def exportar_pdf_embarque(request, embarque_id):
    embarque = get_object_or_404(Embarque, pk=embarque_id)
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Detalles del embarque
    c.drawString(100, 750, f"Reporte de Embarque - Número: {embarque.numero_embarque}")
    c.drawString(100, 730, f"Estado: {embarque.estado}")
    c.drawString(100, 710, f"Exportador: {embarque.exportador}")
    c.drawString(100, 690, f"Importador: {embarque.importador}")
    c.showPage()
    c.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_embarque_{embarque.numero_embarque}.pdf"'
    return response

