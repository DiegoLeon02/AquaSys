from django.shortcuts import render, redirect, get_object_or_404
from .models import EncuestaSatisfaccion, PublicacionRedesSociales, CampaniaPublicitaria
from .forms import EncuestaSatisfaccionForm, PublicacionRedesSocialesForm, CampaniaPublicitariaForm

def marketing_home(request):
    return render(request, 'Marketing.html')
def enviar_encuesta(request):
    if request.method == 'POST':
        form = EncuestaSatisfaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marketing')
    else:
        form = EncuestaSatisfaccionForm()
    return render(request, 'enviar_encuesta.html', {'form': form})

# Vista para programar publicaciones en redes sociales
def programar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionRedesSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marketing')
    else:
        form = PublicacionRedesSocialesForm()
    return render(request, 'programar_publicacion.html', {'form': form})

# Vista para analizar campañas publicitarias
def analizar_campania(request, campania_id):
    campania = get_object_or_404(CampaniaPublicitaria, id=campania_id)
    form = CampaniaPublicitariaForm(instance=campania)
    if request.method == 'POST':
        form = CampaniaPublicitariaForm(request.POST, instance=campania)
        if form.is_valid():
            form.save()
            return redirect('lista_campanias')
    return render(request, 'analizar_campania.html', {'form': form, 'campania': campania})

# Vista para listar todas las campañas publicitarias
def lista_campanias(request):
    campanias = CampaniaPublicitaria.objects.all()
    return render(request, 'lista_campanias.html', {'campanias': campanias})

from django.contrib import admin
from .models import CampaniaPublicitaria

@admin.register(CampaniaPublicitaria)
class CampaniaPublicitariaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'presupuesto')

def crear_campania(request):
    if request.method == 'POST':
        form = CampaniaPublicitariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campanias')
    else:
        form = CampaniaPublicitariaForm()
    return render(request, 'crear_campania.html', {'form': form})
 
def editar_campania(request, campania_id):
    campania = get_object_or_404(CampaniaPublicitaria, id=campania_id)
    if request.method == 'POST':
        form = CampaniaPublicitariaForm(request.POST, instance=campania)
        if form.is_valid():
            form.save()
            return redirect('lista_campanias')
    else:
        form = CampaniaPublicitariaForm(instance=campania)
    return render(request, 'editar_campania.html', {'form': form, 'campania': campania})   
def eliminar_campania(request, campania_id):
    campania = get_object_or_404(CampaniaPublicitaria, id=campania_id)
    if request.method == 'POST':
        campania.delete()
        return redirect('lista_campanias')
    return render(request, 'confirmar_eliminar.html', {'campania': campania})