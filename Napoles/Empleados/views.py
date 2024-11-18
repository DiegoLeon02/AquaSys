from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Empleado
from .forms import EmpleadoForm

# Vista para mostrar la lista de empleados
def lista_empleados(request):
    ordenar_por = request.GET.get('ordenar', None)
    if ordenar_por == 'nombre':
        empleados = Empleado.objects.all().order_by('nombre')  
    else:
        empleados = Empleado.objects.all().order_by('fecha_nacimiento')  

    # Paginación
    paginator = Paginator(empleados, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'empleados.html', {'page_obj': page_obj})

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
