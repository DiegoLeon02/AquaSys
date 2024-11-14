from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Embarque
from .forms import EmbarqueForm

# Create your views here.
def Embarques(request):
    return render(request, 'Embarques.html')


# Vista para listar los embarques
def lista_embarques(request):
    embarques = Embarque.objects.all().order_by('numero_embarque')
    return render(request, 'embarques.html', {'embarques': embarques})

# Vista para crear un nuevo embarque
def crear_embarque(request):
    if request.method == 'POST':
        form = EmbarqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_embarques')
    else:
        form = EmbarqueForm()
    return render(request, 'embarques_form.html', {'form': form})

# Vista para editar un embarque existente
def editar_embarque(request, embarque_id):
    embarque = get_object_or_404(Embarque, id=embarque_id)
    if request.method == 'POST':
        form = EmbarqueForm(request.POST, instance=embarque)
        if form.is_valid():
            form.save()
            return redirect('lista_embarques')
    else:
        form = EmbarqueForm(instance=embarque)
    return render(request, 'embarques_form.html', {'form': form})

# Vista para eliminar un embarque
def eliminar_embarque(request, embarque_id):
    embarque = get_object_or_404(Embarque, id=embarque_id)
    if request.method == 'POST':
        embarque.delete()
        return redirect('lista_embarques')
    return render(request, 'confirmar_eliminacion.html', {'embarque': embarque})
