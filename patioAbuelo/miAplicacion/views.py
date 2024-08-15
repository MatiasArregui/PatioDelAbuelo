from django.shortcuts import render
from .models import Bebida, Plato, Postre, Cliente, Mesa, Orden, Factura

# Create your views here.
def principal(request):
    return render(request, template_name="base.html")

def listaBebidas(request):
    bebidas = Bebida.objects.all()
    context = {"bebidas":bebidas}
    return render(request, template_name="listaBebidas.html", context=context)

def listaPlatos(request):
    platos = Plato.objects.all()
    context = {"platos":platos}
    return render(request, template_name="listaPLatos.html", context=context)

def listaPostres(request):
    postres = Postre.objects.all()
    context = {"postres":postres}
    return render(request, template_name="listaPostres.html", context=context)

def listaMesas(request):
    mesas = Mesa.objects.all()
    context = {"mesa": mesas}
    return render(request, template_name="listaMesas.html", context=context)

def listaClientes(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, template_name="listaClientes.html", context=context)
