from django import forms

from apps.vianda.models import Tipo_Plato, Vianda

class TipoPlatosForm(forms.ModelForm):
     class Meta:        
         model = Tipo_Plato
         fields = ('descripcion','vigencia')
         prefix = 'tipoplato'
    

class ViandaForm(forms.ModelForm):
     class Meta:        
         model = Vianda
         fields = ('frecuencia','tipo_menu','fecha_inicio_vianda','cantidad','estado','tipo_platos')
         prefix = 'vianda'
         widgets = {
        'fecha_inicio_vianda': forms.DateInput(attrs={ 'type':"date"}),
         }

