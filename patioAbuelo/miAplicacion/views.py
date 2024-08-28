from django.shortcuts import render, HttpResponseRedirect
from .models import Bebida, Plato, Postre, Cliente, Mesa, Orden, Factura
from django.urls import reverse

# Create your views here.
def principal(request):
    return render(request, template_name="base.html")

def listaPlatos(request):
    platos = Plato.objects.all()
    context = {"platos":platos}
    return render(request, template_name="listaPLatos.html", context=context)

# BEBIDA VIEWS ----------------------------------------------------------------------------------------->
# Listado Bebida ------->
def listaBebidas(request):
    bebidas = Bebida.objects.all()
    context = {"bebidas":bebidas}
    return render(request, template_name="listaBebidas.html", context=context)

# Modificar Bebida --------->
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

# Nueva Bebida ------------------>
def bebidaNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        Bebida.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, "formularioBebidas.html")

# Borrar Bebida ----------------------->
def bebidaBorrar(request, pk):
    bebida = Bebida.objects.get(id=pk)
    if request.method == 'POST':
        bebida.delete()
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, 'bebidaConfBorrar.html', {'bebida': bebida})


# ORDEN VIEWS ---------------------------------------------------------------------------------------------->
# Listado Orden ------->
def listaOrdenes(request):
    ordenes = Orden.objects.all()
    context = {"ordenes": ordenes}
    return render(request, template_name="listaOrdenes.html", context=context)

# Modificar Orden --------->
def ordenModificar(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        total = request.POST.get('total')
        observacion = request.POST.get('observacion')

        orden.total = total
        orden.observacion = observacion
        orden.save()
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, "formularioOrdenes.html", {'orden': orden})

# Nueva Orden ------------------>
def ordenNuevo(request):
    if request.method == 'POST':
        total = request.POST.get('total')
        observacion = request.POST.get('observacion')

        Orden.objects.create(total=total, observacion=observacion,)
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, "formularioOrdenes.html")

# Borrar Orden ----------------------->
def ordenBorrar(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, 'ordenConfBorrar.html', {'orden': orden})

# CIENTES VIEWS ---------------------------------------------------------------------------------------------->
# Listado Cliente -------
def listaClientes(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, template_name="listaClientes.html", context=context)

# Modificar Cliente --------->
def clientesModificar(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.save()
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, "formularioClientes.html", {'cliente': cliente})

# Nuevo Cliente ------------------>
def clientesNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        Cliente.objects.create(nombre=nombre, telefono=telefono, direccion=direccion)
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, "formularioClientes.html")

# Borrar Cliente ----------------------->
def clientesBorrar(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, 'clienteConfBorrar.html', {'cliente': cliente})

# POSTRE VIEWS ------------------------------------------------------------------------------>
# Postre --------------------------->
def listaPostre(request):
    postre = Postre.objects.all()
    context = {"postre": postre}
    return render(request, template_name="listaPostres.html", context=context)
# Modificar postre ------------->
def postreModificar(request, pk):
    postre = Postre.objects.get(id=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        postre.nombre = nombre
        postre.precio = precio
        postre.cantidad = cantidad
        postre.save()
        return HttpResponseRedirect(reverse('listaPostre'))
    return render(request, "formularioPostre.html", {'postre': postre})

# Nueva postre ------------------>
def postreNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        Postre.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaPostre'))
    return render(request, "formularioPostre.html")

# Borrar postre ----------------------->
def postreBorrar(request, pk):
    postre = Postre.objects.get(id=pk)
    if request.method == 'POST':
        postre.delete()
        return HttpResponseRedirect(reverse('listaPostre'))
    return render(request, 'postreConfBorrar.html', {'postre': postre})

# MESAS VIEWS ----------------------------------->
# Listado Mesa ------->
def listaMesas(request):
    mesas = Mesa.objects.all()
    context = {"mesas":mesas}
    return render(request, template_name="listaMesas.html", context=context)

# Modificar Mesa --------->
def mesaModificar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    context = {'mesa': mesa}
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')

        mesa.nombre = nombre
        mesa.cantidad = cantidad
        mesa.save()
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, "formularioMesas.html", context=context)
# Nueva Mesa --------->
def mesaNueva(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')

        Mesa.objects.create(nombre=nombre, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, "formularioMesas.html")

# Borrar Mesa ----------------------->
def mesaBorrar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    if request.method == 'POST':
        mesa.delete()
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, 'mesaConfBorrar.html', {'mesa': mesa})