from django.contrib import admin

from apps.vianda.models import Tipo_Plato, Vianda

# Register your models here.


admin.site.register(Vianda)
admin.site.register(Tipo_Plato)
