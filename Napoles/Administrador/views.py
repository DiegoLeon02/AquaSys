from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm, LoginForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import LoginActivity, Perfil
from .forms import LoginForm
import openpyxl
from django.http import HttpResponse
from .models import LoginActivity

# Vista principal del Administrador
@login_required
def administrador(request):
    return render(request, 'administrador.html')


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


# Vista para eliminar un perfil con confirmación
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


# Vista para login externo
def external_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                # Busca el usuario y perfil
                user = User.objects.get(email=email)
                perfil = Perfil.objects.get(email=email)
                user_authenticated = authenticate(username=user.username, password=password)

                if user_authenticated:
                    # Login exitoso
                    login(request, user_authenticated)

                    # Registra la actividad
                    LoginActivity.objects.create(
                        perfil=perfil,
                        exitoso=True,
                        mensaje="Inicio de sesión exitoso"
                    )
                    return redirect('administrador')  
                else:
                    # Login fallido (contraseña incorrecta)
                    LoginActivity.objects.create(
                        perfil=perfil,
                        exitoso=False,
                        mensaje="Contraseña incorrecta"
                    )
                    form.add_error(None, 'Contraseña incorrecta')

            except User.DoesNotExist:
                # Usuario no encontrado
                LoginActivity.objects.create(
                    perfil=None,
                    exitoso=False,
                    mensaje=f"El email {email} no está registrado"
                )
                form.add_error(None, 'Usuario no encontrado')
    else:
        form = LoginForm()

    return render(request, 'external_login.html', {'form': form})

#/////////////////////////////////////////////////////////////////////////
def exportar_excel(request):
    # Crear un libro de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Actividades"

    # Encabezados del archivo
    ws.append(['Nombre del Perfil', 'Fecha y Hora', 'Resultado', 'Mensaje'])

    # Obtener datos de la tabla LoginActivity
    actividades = LoginActivity.objects.select_related('perfil').all()
    for actividad in actividades:
        ws.append([
            actividad.perfil.nombre if actividad.perfil else 'Sin perfil',  
            actividad.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Exitoso' if actividad.exitoso else 'Fallido',
            actividad.mensaje or 'N/A'
        ])

    # Configurar la respuesta HTTP para descargar el archivo
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="reporte_actividades.xlsx"'

    # Guardar el archivo Excel
    wb.save(response)
    return response