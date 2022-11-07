from django.urls import path

from apps.usuario import views
from apps.vianda.views import crear_vianda, lista_vianda
from apps.vianda import views

app_name = 'vianda'
urlpatterns = [
    path("verlista/",lista_vianda, name="listavianda"),
    path("crear/", crear_vianda, name="crearvianda"),
 ]
