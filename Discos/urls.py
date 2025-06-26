from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion2', views.Discos1, name='Discos.html'),
]
