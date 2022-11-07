from django.shortcuts import redirect, render
from django.urls import reverse
from requests import request

from apps.vianda.forms import TipoPlatosForm, ViandaForm

# Create your views here.


#@login_required(login_url='usuario:login')
#@permission_required('Plato.add_plato', raise_exception=True)
def crear_vianda(request):
    if (request.method == 'POST'):
        tipoplato_form = TipoPlatosForm(request.POST, prefix='tipopplato')
        vianda_form = ViandaForm(request.POST, prefix='vianda')
        if vianda_form.is_valid() and tipoplato_form.is_valid():
            vianda=vianda_form.save(commit=False)
            
            return redirect(reverse('usuario:index', args={vianda.codigo_plato}))
    else:
          vianda_form = ViandaForm(prefix='menu')
    return render(request,'vianda/crear.html',{'vianda_form': vianda_form})
