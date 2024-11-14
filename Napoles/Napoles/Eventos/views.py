from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

# Create your views here.
def Eventos(request):
    return render(request, 'Eventos.html')

# Vista para mostrar la lista de eventos
def lista_eventos(request):
    eventos = Evento.objects.all().order_by('fecha')
    return render(request, 'eventos.html', {'eventos': eventos})

# Vista para crear un evento
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos') 
    else:
        form = EventoForm()
    return render(request, 'eventos_form.html', {'form': form})

# Vista para editar un evento
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos_form.html', {'form': form})

# Vista para eliminar un evento
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')  
    return render(request, 'confirmar_eliminacion.html', {'evento': evento})
