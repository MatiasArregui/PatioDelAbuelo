from django.shortcuts import render, HttpResponseRedirect
from .models import Orden, Carta, Factura, Cliente, Mesa, Mozo, SubCategoria, Categoria
from .forms import MozoForm, ClienteForm, CartaForm
from django.urls import reverse

# Pagina principal ----------------------------------------------------------------------------------->
def principal(request):
    return render(request, template_name="base.html")

# Login de ingreso ------------------------------------------------------------------------------------->
def loginIngreso(request):
    return render(request, template_name="login.html")

# PLATO VIEWS ------------------------------------------------------------------------------>
# Listado plato --------------------------->
def listaCarta(request):
    carta = Carta.objects.all()
    context = {"carta": carta}
    return render(request, template_name="./listas/listaCarta.html", context=context)

# Modificar plato ------------->
def cartaModificar(request, pk):
    carta = Carta.objects.get(id=pk)
    categorias = [{"value":x.pk, "text":x.nombre} for x in Categoria.objects.all()]
    opcion1 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk} for x in SubCategoria.objects.filter(id_categoria=1)]
    opcion2 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk}for x in SubCategoria.objects.filter(id_categoria=2)]
    opcion3 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk} for x in SubCategoria.objects.filter(id_categoria=3)]
    if request.method == 'POST':
        form = CartaForm(request.POST, instance=carta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaCarta'))
    else:
        form = CartaForm(instance=carta)
    return render(request, './formularios/formularioCarta.html', {'form': form, 'carta': carta, "opcion1":opcion1, "opcion2":opcion2, "opcion3":opcion3, "categorias":categorias})

# Nuevo plato ------------------>
def cartaNuevo(request):
    categorias = [{"value":x.pk, "text":x.nombre} for x in Categoria.objects.all()]
    opcion1 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk} for x in SubCategoria.objects.filter(id_categoria=1)]
    opcion2 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk}for x in SubCategoria.objects.filter(id_categoria=2)]
    opcion3 = [{"value":x.pk, "text":x.nombre, "id_categoria":x.id_categoria.pk} for x in SubCategoria.objects.filter(id_categoria=3)]
    # valoresPlato = [x.pk for x in SubCategoria.objects.filter(id_categoria=1)]
    # valoresBebida = [x.pk for x in SubCategoria.objects.filter(id_categoria=2)]
    # valoresPostre = [x.pk for x in SubCategoria.objects.filter(id_categoria=3)]
    # print(opcionesPlato)
    # print(opcionesBebida)
    # print(opcionesPostre)
    if request.method == 'POST':
        form = CartaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaCarta'))
    else:
        form = CartaForm()
    return render(request, './formularios/formularioCarta.html', {'form': form, "opcion1":opcion1, "opcion2":opcion2, "opcion3":opcion3, "categorias":categorias})

# Borrar plato ----------------------->
def cartaBorrar(request, pk):
    carta = Carta.objects.get(id=pk)
    if request.method == 'POST':
        carta.delete()
        return HttpResponseRedirect(reverse('listaCarta'))
    return render(request, './confirmacionBorrado/cartaConfBorrar.html', {'carta': carta})

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
    context = {"clientes":clientes}
    return render(request, template_name="./listas/listaClientes.html", context=context)

# Modificar Cliente --------->
def ClienteModif(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaClientes'))
    else:
        form = ClienteForm(instance=cliente)
    return render(request, './formularios/formularioClientes.html', {'form': form, 'mozo': cliente})
#
# Nuevo Cliente ------------------>
def ClienteNuevo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaClientes'))
    else:
        form = ClienteForm()
    return render(request, './formularios/formularioClientes.html', {'form': form})

# Borrar Cliente ----------------------->
def ClienteBorrar(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('listaClientes'))
    return render(request, './confirmacionBorrado/clienteConfBorrar.html', {'cliente': cliente})

# MOZO VIEWS ----------------------------------------------------------------------------------------->
#Listado Mozos ------------------------------------->
def listaMozos(request):
    mozos = Mozo.objects.all()
    context = {"mozos":mozos}
    return render(request, template_name="./listas/listaMozos.html", context=context)
#Mozo modificar ---------------------------------->
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
# Mozo nuevo -------------------------------------------->
def MozoNuevo(request):
    if request.method == 'POST':
        form = MozoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMozos'))
    else:
        form = MozoForm()
    return render(request, './formularios/formularioMozos.html', {'form': form})
#Mozo borrar ----------------------------------------------->
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
