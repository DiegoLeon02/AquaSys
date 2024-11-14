from django.urls import path
from . import views

urlpatterns = [
    path('Marketing/', views.marketing_home, name='Marketing'),
    path('Marketing/enviar_encuesta/', views.enviar_encuesta, name='enviar_encuesta'),
    path('Marketing/programar_publicacion/', views.programar_publicacion, name='programar_publicacion'),
    path('Marketing/analizar_campania/<int:campania_id>/', views.analizar_campania, name='analizar_campania'),
    path('Marketing/lista_campanias/', views.lista_campanias, name='lista_campanias'),
    path('Marketing/crear_campania/', views.crear_campania, name='crear_campania'),
    path('Marketing/editar_campania/<int:campania_id>/', views.editar_campania, name='editar_campania'),
    path('Marketing/eliminar_campania/<int:campania_id>/', views.eliminar_campania, name='eliminar_campania'),
]
