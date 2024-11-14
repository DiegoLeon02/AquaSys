from django.urls import path
from . import views

urlpatterns = [
    path('reportes/', views.lista_reportes, name='reportes'),
    path('reportes/login_activity/<int:actividad_id>/pdf/', views.exportar_pdf_login_activity, name='descargar_pdf_login_activity'),
    path('reportes/embarque/<int:embarque_id>/pdf/', views.exportar_pdf_embarque, name='descargar_pdf_embarque'),
]
