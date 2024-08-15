from django.shortcuts import render, HttpResponseRedirect
from .models import Bebida, Plato, Postre, Cliente, Mesa, Orden, Factura
from django.urls import reverse

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


def bebidaModificar(request, pk):
    bebida = Bebida.objects.get(id=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        bebida.nombre = nombre
        bebida.precio = precio
        bebida.cantidad = cantidad
        bebida.save()
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, "formularioBebidas.html", {'bebida': bebida})


def bebidaNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        Bebida.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, "formularioBebidas.html")


def bebidaBorrar(request, pk):
    bebida = Bebida.objects.get(id=pk)
    if request.method == 'POST':
        bebida.delete()
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, 'bebidaConfBorrar.html', {'bebida': bebida})
