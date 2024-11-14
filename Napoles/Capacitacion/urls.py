from django.urls import path
from . import views

urlpatterns = [
   path('Capacitacion/', views.Capacitacion, name='Capacitacion'),
   
]