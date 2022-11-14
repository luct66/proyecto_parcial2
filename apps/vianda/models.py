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
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tipo_Plato(models.Model):
    descripcion = models.CharField(max_length=200)
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
    frecuencia = models.CharField(choices=frecuencias,max_length=200)
    tipo_menu = models.CharField(choices=tiposmenus,max_length=200)
    fecha_inicio_vianda = models.DateField()
    cantidad = models.IntegerField(default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    estado = models.CharField(choices=estados,max_length=200,default='Pendiente')
    tipo_platos = models.ManyToManyField(Tipo_Plato)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        texto = "{0}-{1}-{2}-{3}"
        return texto.format(self.frecuencia,self.cantidad,self.tipo_menu,self.tipo_platos.descripcion)
