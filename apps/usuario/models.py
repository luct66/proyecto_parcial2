from django.db import models

# Create your models here.


# # Modelos
# from cgitb import text
# from email.policy import default
# from enum import unique
# from random import choices
# from re import S
# from secrets import choice
# from tkinter import CASCADE
# from django.db import models
# from django.contrib.auth.models import User

# from django.db import models

# class Persona(models.Model):
#     cuil = models.CharField(max_length=11, unique=True)
#     nombre = models.CharField(max_length=200, blank= True)
#     apellido = models.CharField(max_length=200, blank= True)
#     fecha_nacimiento = models.DateField(blank= True)
#     email = models.CharField(max_length=300,blank= True)
#     domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, default=None)
#     telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=None)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)

#     def __str__(self):
#         texto = "{0} - {1} - {2} - {3} - {4} "
#         return texto.format(self.cuil, self.apellido, self.nombre, self.fecha_nacimiento, self.domicilio)

