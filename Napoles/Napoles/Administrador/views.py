from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm, LoginForm  
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Vista para listar perfiles
@login_required
def lista_perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'administracion_perfiles.html', {'perfiles': perfiles})

# Vista para crear un nuevo perfil
@login_required
def crear_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perfiles')
    else:
        form = PerfilForm()
    return render(request, 'perfil_form.html', {'form': form})

# Vista para editar un perfil
@login_required
def editar_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('lista_perfiles')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil_form.html', {'form': form})

# Vista para eliminar un perfil
@login_required
def eliminar_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('lista_perfiles')
    return render(request, 'confirmar_eliminacion.html', {'perfil': perfil})

# Vista para logout
def logout_view(request):
    logout(request)
    return redirect('external_login')  

# Vista principal del Administrador
def Administrador(request):
    return render(request, 'Administrador.html')

# Vista para login externo
def external_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('index')  
                else:
                    form.add_error(None, 'Email o contraseña incorrectos')
            except User.DoesNotExist:
                form.add_error(None, 'Usuario no encontrado')
    else:
        form = LoginForm()

    return render(request, 'external_login.html', {'form': form})
