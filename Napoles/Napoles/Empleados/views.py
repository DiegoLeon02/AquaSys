from django.shortcuts import render,redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

def Empleados(request):
    return render(request, 'Empleados.html')  

# Vista para mostrar la lista de empleados
def lista_empleados(request):
    empleados = Empleado.objects.all().order_by('fecha_nacimiento')
    return render(request, 'empleados.html', {'empleados': empleados})

# Vista para crear un empleado
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados') 
    else:
        form = EmpleadoForm()
    return render(request, 'empleados_form.html', {'form': form})

# Vista para editar un empleado
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')  
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados_form.html', {'form': form})

# Vista para eliminar un empleado
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')  
    return render(request, 'confirmar_eliminacion.html', {'empleado': empleado})