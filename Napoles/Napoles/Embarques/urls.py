from django.urls import path
from . import views

urlpatterns = [
   path('Embarques/', views.lista_embarques, name='Embarques'),
    path('', views.lista_embarques, name='lista_embarques'),
    path('crear/', views.crear_embarque, name='crear_embarque'),
    path('editar/<int:embarque_id>/', views.editar_embarque, name='editar_embarque'),
    path('eliminar/<int:embarque_id>/', views.eliminar_embarque, name='eliminar_embarque'),
]