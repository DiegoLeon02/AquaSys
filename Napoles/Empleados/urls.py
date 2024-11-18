from django.urls import path
from . import views

urlpatterns = [
    path('Empleados/', views.lista_empleados, name='Empleados'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
]