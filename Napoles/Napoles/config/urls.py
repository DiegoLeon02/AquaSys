from django.contrib import admin
from django.urls import path, include  # Agrega include
from . import views  # Asegúrate de importar views
import Administrador.views as Administrador_views

urlpatterns = [
    path('', Administrador_views.external_login, name='external_login'),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # Agrega esta línea para la URL raíz
    path('index/', views.index, name='index'),  # Esta sigue siendo tu URL /index/
    path('Administrador/', include('Administrador.urls')), 
    path('Embarques/', include('Embarques.urls')),  # Agrega esta línea
    path('Eventos/', include('Eventos.urls')),  # Agrega esta línea
    path('Empleados/', include('Empleados.urls')),  # Agrega esta línea
    path('Capacitacion/', include('Capacitacion.urls')),  # Agrega esta línea
    path('Marketing/', include('Marketing.urls')),  # Agrega esta línea
    path('Reportes/', include('Reportes.urls')),  # Agrega esta línea
]

