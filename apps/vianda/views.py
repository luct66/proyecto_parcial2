from django.shortcuts import redirect, render
from django.urls import reverse
from requests import request
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
# from apps import vianda
from apps.vianda.models import Vianda
from django.contrib.auth.models import User

from apps.vianda.forms import TipoPlatosForm, ViandaForm

# Create your views here.


@login_required(login_url='usuario:login')
@permission_required('vianda.add_plato', raise_exception=True)
def crear_vianda(request):
    if (request.method == 'POST'):
        tipoplato_form = TipoPlatosForm(request.POST, prefix='tipopplato')
        vianda_form = ViandaForm(request.POST, prefix='vianda')
        if vianda_form.is_valid() and tipoplato_form.is_valid():
            v=vianda_form.save(commit=False)
            obtener_id_user = request.POST['id']
            v.user_id=obtener_id_user
            v.save()

            return render(request,'base/index.html')
    else:
          vianda_form = ViandaForm(prefix='menu')
    return render(request,'vianda/crear.html',{'vianda_form': vianda_form})

@login_required(login_url='Usuario:login')
#@permission_required('vianda.view_pedido', raise_exception=True)
def lista_vianda(request):
    listavianda = Vianda.objects.all()
    return render(request,'vianda/lista.html',{'viandas': listavianda})
