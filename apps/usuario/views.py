from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


@login_required(login_url='usuario:login')
def index(request):
    return render(request, "base/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "usuario/login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuario/login.html", {"msj": "Deslogueado"})




# # Creacion

# @login_required(login_url='Usuario:login')
# @permission_required('Plato.add_plato', raise_exception=True)
# def creacion_menu(request):
#     if (request.method == 'POST'):
#         plato_form = PlatoForm(request.POST, prefix='menu')
#         if plato_form.is_valid():
#             p=plato_form.save(commit=True)
#             return redirect(reverse('Pedido:menu_detalle', args={p.codigo_plato}))
#     else:
#         plato_form = PlatoForm(prefix='menu')
#     return render(request,'Pedido/RegistroDeMenu.html',{'plato_form': plato_form})

# # Detalle

# @login_required(login_url='Usuario:login')
# def menu_detalle(request, pk):
#     plato = get_object_or_404(Plato, pk=pk)
#     return render(request,'Pedido/detalle.html',{'plato': plato})

# # Delete

# @login_required(login_url='Usuario:login')
# def menu_delete(request):
#     if request.method == 'POST':
#         if 'codigo_plato' in request.POST:
#             menu = get_object_or_404(Plato, pk=request.POST['codigo_plato'])
#             menu.delete()
#             messages.success(request,
#             'Se ha eliminado la persona {}'.format(menu))
#     menus = Plato.objects.all()
#     return render(request,'Pedido/listademenus.html',{'menus': menus})

# # Editar

# @login_required(login_url='Usuario:login')
# def pedido_edit(request, pk):
#     pedido = get_object_or_404(Pedido, pk=pk)
#     pedido_form = PedidoCadeteForm(request.POST,prefix='pedido',instance=pedido)
#     if request.method == 'POST' :
#         if pedido_form.is_valid():
#             p=pedido_form.save(commit=False)
#             p.save()
#             messages.success(request,
#             'Se ha agregado correctamente la persona {}'.format(p))
#             return redirect(reverse('Pedido:detalle_pedido', args={p.cod_pedido}))
#     else:   
#         pedido_form = PedidoCadeteForm(prefix='pedido')
#     return render(request,'Pedido/editar_pedido.html',{'pedido_form':pedido_form,'pedido':pedido})


# # Lista
# @login_required(login_url='Usuario:login')
# @permission_required('Pedido.view_pedido', raise_exception=True)
# def lista_pedidos(request):
#     listaPedidos = Pedido.objects.all()
#     return render(request,'Pedido/ListaDepedidos.html',{'pedidos': listaPedidos})

# # Buscar

# @login_required(login_url='Usuario:login')
# def buscar_platosadmin(request):
#     platos = Plato.objects.all()
#     if 'buscar' in request.GET:
#         buscar_plato = platos.filter(nombre_plato__icontains=request.GET['buscar'])
#     print(request.GET['buscar'])
#     return render(request, 'Pedido/listademenus.html',
#                   {'menus': buscar_plato})

