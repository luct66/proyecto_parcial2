from django.db import models
from cgitb import text
from email.policy import default
from enum import unique
from random import choices
from re import S
from secrets import choice
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tipo_Plato(models.Model):
    descripcion = models.CharField(max_length=200, blank= True)
    vigencia = models.BooleanField(default=True)


    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion)


class Vianda(models.Model):

    tiposmenus=(
        ('Normal','normal'),
        ('Diabetico','diabetico'),
        ('Vegetariano','vegetariano'),
    )
    frecuencias=(
        ('Semanal','semanal'),
        ('Quincenal','quincenal'),
    )
    estados=(
        ('Pendiente','pendiente'),
        ('Confirmado','confirmado'),
        ('Cancelado','cancelado'),

    )
    frecuencia = models.CharField(choices=frecuencias,max_length=200, blank= True)
    tipo_menu = models.CharField(choices=tiposmenus,max_length=200, blank= True)
    fecha_inicio_vianda = models.DateField(blank = True)
    cantidad = models.IntegerField(default=1)
    estado = models.CharField(choices=estados,max_length=200,default='Pendiente' ,blank= True)
    tipo_platos = models.ForeignKey(Tipo_Plato, on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)


    def __str__(self):
        texto = "{0}"
        return texto.format(self.tipo_platos.descripcion)
