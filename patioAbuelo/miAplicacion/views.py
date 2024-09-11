from django.shortcuts import render, HttpResponseRedirect
from .models import Bebida, Plato, Postre, Cliente, Mesa, Orden, Factura, Mozo
from .forms import MozoForm
from django.urls import reverse

# Pagina principal ----------------------------------------------------------------------------------->
def principal(request):
    return render(request, template_name="base.html")

# Login de ingreso ------------------------------------------------------------------------------------->
def loginIngreso(request):
    return render(request, template_name="login.html")


# BEBIDA VIEWS ----------------------------------------------------------------------------------------->
# Listado Bebida ------->
def listaBebidas(request):
    bebidas = Bebida.objects.all()
    context = {"bebidas":bebidas}
    return render(request, template_name="./listas/listaBebidas.html", context=context)

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
    return render(request, "./formularios/formularioBebidas.html", {'bebida': bebida})

# Nueva Bebida ------------------>
def bebidaNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        Bebida.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, "./formularios/formularioBebidas.html")

# Borrar Bebida ----------------------->
def bebidaBorrar(request, pk):
    bebida = Bebida.objects.get(id=pk)
    if request.method == 'POST':
        bebida.delete()
        return HttpResponseRedirect(reverse('listaBebidas'))
    return render(request, './confirmacioBorrado/bebidaConfBorrar.html', {'bebida': bebida})

# PLATO VIEWS ------------------------------------------------------------------------------>
# Listado plato --------------------------->
def listaPlato(request):
    platos = Plato.objects.all()
    context = {"platos": platos}
    return render(request, template_name="./listas/listaPlatos.html", context=context)
# Modificar plato ------------->
def platoModificar(request, pk):
    plato = Plato.objects.get(id=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')

        plato.nombre = nombre
        plato.precio = precio
        plato.save()
        return HttpResponseRedirect(reverse('listaPlatos'))
    return render(request, "./formularios/formularioPlatos.html", {'plato': plato})

# Nuevo plato ------------------>
def platoNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')

        Plato.objects.create(nombre=nombre, precio=precio)
        return HttpResponseRedirect(reverse('listaPlatos'))
    return render(request, "./formularios/formularioPlatos.html")

# Borrar plato ----------------------->
def platoBorrar(request, pk):
    plato = Plato.objects.get(id=pk)
    if request.method == 'POST':
        plato.delete()
        return HttpResponseRedirect(reverse('listaPlatos'))
    return render(request, './confirmacionBorrado/platoConfBorrar.html', {'plato': plato})

# POSTRE VIEWS ------------------------------------------------------------------------------>
# Postre --------------------------->
def listaPostre(request):
    postres = Postre.objects.all()
    context = {"postres": postres}
    return render(request, template_name="./listas/listaPostres.html", context=context)
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
        return HttpResponseRedirect(reverse('listaPostres'))
    return render(request, "./formularios/formularioPostres.html", {'postre': postre})

# Nueva postre ------------------>
def postreNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        Postre.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return HttpResponseRedirect(reverse('listaPostres'))
    return render(request, "./formularios/formularioPostres.html")

# Borrar postre ----------------------->
def postreBorrar(request, pk):
    postre = Postre.objects.get(id=pk)
    if request.method == 'POST':
        postre.delete()
        return HttpResponseRedirect(reverse('listaPostres'))
    return render(request, './confirmacionBorrado/postreConfBorrar.html', {'postre': postre})

# MESAS VIEWS ----------------------------------->
# Listado Mesa ------->
def listaMesas(request):
    mesas = Mesa.objects.all()
    context = {"mesas":mesas}
    return render(request, template_name="./listas/listaMesas.html", context=context)

# Modificar Mesa --------->
def mesaModificar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    context = {'mesa': mesa}
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        mesa.nombre = nombre
        mesa.save()
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, "./formularios/formularioMesas.html", context=context)
# Nueva Mesa --------->
def mesaNueva(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        Mesa.objects.create(nombre=nombre,)
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, "./formularios/formularioMesas.html")

# Borrar Mesa ----------------------->
def mesaBorrar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    if request.method == 'POST':
        mesa.delete()
        return HttpResponseRedirect(reverse('listaMesas'))
    return render(request, './confirmacionBorrado/mesaConfBorrar.html', {'mesa': mesa})

# CIENTES VIEWS ---------------------------------------------------------------------------------------------->
# Listado Cliente -------
def listaClientes(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, template_name="./listas/listaClientes.html", context=context)

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
    return render(request, "./formularios/formularioClientes.html", {'cliente': cliente})

# Nuevo Cliente ------------------>
def clientesNuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        Cliente.objects.create(nombre=nombre, telefono=telefono, direccion=direccion)
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, "./formularios/formularioClientes.html")

# Borrar Cliente ----------------------->
def clientesBorrar(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, './confirmacionBorrado/clienteConfBorrar.html', {'cliente': cliente})

# MOZO VIEWS ----------------------------------------------------------------------------------------->
def listaMozos(request):
    mozos = Mozo.objects.all()
    context = {"mozos":mozos}
    return render(request, template_name="./listas/listaMozos.html", context=context)

def MozoModif(request, pk):
    mozo = Mozo.objects.get(id=pk)
    if request.method == 'POST':
        form = MozoForm(request.POST, instance=mozo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMozos'))
    else:
        form = MozoForm(instance=mozo)
    return render(request, './formularios/formularioMozos.html', {'form': form, 'mozo': mozo})


def MozoNuevo(request):
    if request.method == 'POST':
        form = MozoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMozos'))
    else:
        form = MozoForm()
    return render(request, './formularios/formularioMozos.html', {'form': form})


def MozoBorrar(request, pk):
    mozo = Mozo.objects.get(id=pk)
    if request.method == 'POST':
        mozo.delete()
        return HttpResponseRedirect(reverse('listaMozos'))
    return render(request, './confirmacionBorrado/mozoConfBorrar.html', {'mozo': mozo})

# ORDEN VIEWS ---------------------------------------------------------------------------------------------->
# Listado Orden ------->
def listaOrdenes(request):
    ordenes = Orden.objects.all()
    context = {"ordenes": ordenes}
    return render(request, template_name="./listas/listaOrdenes.html", context=context)

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
    return render(request, "./formularios/formularioOrdenes.html", {'orden': orden})

# Nueva Orden ------------------>
def ordenNuevo(request):
    if request.method == 'POST':
        total = request.POST.get('total')
        observacion = request.POST.get('observacion')

        Orden.objects.create(total=total, observacion=observacion,)
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, "./formularios/formularioOrdenes.html")

# Borrar Orden ----------------------->
def ordenBorrar(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, './confirmacionBorrado/ordenConfBorrar.html', {'orden': orden})

# FACTURAS VIEWS ---------------------------------------------------------------------------------------------->
# Factura Orden ------->
def listaFacturas(request):
    facturas = Factura.objects.all()
    context = {"facturas": facturas}
    return render(request, template_name="./listas/listaFacturas.html", context=context)

# Modificar Factura --------->
def facturaModificar(request, pk):
    factura = Factura.objects.get(id=pk)
    if request.method == 'POST':
        total = request.POST.get('total')

        factura.total = total
        factura.save()
        return HttpResponseRedirect(reverse('listaFacturas'))
    return render(request, "./formularios/formularioFacturas.html", {'factura': factura})

# Nueva Factura ------------------>
def facturaNuevo(request):
    if request.method == 'POST':
        total = request.POST.get('total')

        Factura.objects.create(total=total, )
        return HttpResponseRedirect(reverse('listaFacturas'))
    return render(request, "./formularios/formularioFacturas.html")

# Borrar Factura ----------------------->
def facturaBorrar(request, pk):
    factura = Factura.objects.get(id=pk)
    if request.method == 'POST':
        factura.delete()
        return HttpResponseRedirect(reverse('listaFacturas'))
    return render(request, './confirmacionBorrado/facturaConfBorrar.html', {'factura': factura})
