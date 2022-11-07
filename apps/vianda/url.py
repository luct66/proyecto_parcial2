from django.urls import path

from apps.usuario import views
from apps.vianda.views import crear_vianda
from apps.vianda import views

app_name = 'vianda'
urlpatterns = [
    # path("verlista/", views.lista_vista, name="listavista"),
    path("crear/", crear_vianda, name="crearvianda"),
 ]
