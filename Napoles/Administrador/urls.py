from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
  
    path('administrador/', views.lista_perfiles, name='administrador'),
    path('external_login/', views.external_login, name='external_login'),
    path('perfiles/', views.lista_perfiles, name='lista_perfiles'),  
    path('crear/', views.crear_perfil, name='crear_perfil'),        
    path('editar/<int:perfil_id>/', views.editar_perfil, name='editar_perfil'), 
    path('eliminar/<int:perfil_id>/', views.eliminar_perfil, name='eliminar_perfil'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),  
    path('logout/', views.logout_view, name='logout'),  
]
