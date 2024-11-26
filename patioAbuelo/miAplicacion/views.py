from django.shortcuts import render, HttpResponseRedirect
from .models import Orden, Carta, Factura, Cliente, Mesa, Mozo, SubCategoria, Categoria, CartaOrden, FacturaOrden, Cierre, FacturaCierre, PlatoDia
from .forms import MozoForm, ClienteForm, CartaForm, OrdenForm, CartaOrdenFormSet, FacturaForm, FacturaOrdenFormSet, FacturaPagoFormSet, CierreForm,  FacturaCierreFormSet, LoginForm, PlatoDiaForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import random
# from datetime import datetime, timedelta
# import pytz

# Pagina principal ----------------------------------------------------------------------------------->
def principal(request):
    cartaId = [x.pk for x in Carta.objects.all()]
    carta_aleratoria = random.choice(cartaId)
    carta = Carta.objects.get(id=carta_aleratoria)
    platoDia = PlatoDia.objects.all()
    context = {"carta": carta,
               "platoDia":platoDia}
    return render(request, template_name="paginaPrincipal.html", context=context)

# Login de ingreso ------------------------------------------------------------------------------------->
class LoginIngreso(LoginView):
    template_name ="./registration/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("paginaPrincipal")

# PLATO VIEWS ------------------------------------------------------------------------------>
# Listado plato --------------------------->

class listaCarta(ListView):
    model = Carta
    template_name = "./listas/listaCarta.html"
    context_object_name = 'carta'
    paginate_by = 7

    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context


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

    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES)
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
class listaMesas(ListView):
    model = Mesa
    template_name = "./listas/listaMesas.html"
    context_object_name = 'mesa'
    paginate_by = 2


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
class listaClientes(ListView):
    model = Cliente
    template_name = "./listas/listaclientes.html"
    context_object_name = 'clientes'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context
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
class listaMozos(ListView):
    model = Mozo
    template_name = "./listas/listamozos.html"
    context_object_name = 'mozos'
    paginate_by = 2
    

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
class listaOrdenes(ListView):
    model = Orden
    template_name = "./listas/listaOrdenes.html"
    context_object_name = 'ordenes'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(fecha__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context

# # Modificar Orden --------->
# def ordenModificar(request, pk):
#     orden = Orden.objects.get(id=pk)
#     platos = Carta.objects.all()
#     mesas = [{"value":x.pk, "text":x.nombre} for x in Mesa.objects.filter(id=orden.id_mesa.pk)]
#     mesas_2 = [{"value":x.pk, "text":x.nombre} for x in Mesa.objects.filter(estado=False)]
#     mesas.extend(mesas_2)
#     mesa_anterior = orden.id_mesa
#     cantidad_anterior = [{"plato":x.id_carta, "cantidad":x.cantidad} for x in CartaOrden.objects.filter(id_orden=pk)]
#     if request.method == 'POST':
#         orden_form = OrdenForm(request.POST, instance=orden)
#         formset = CartaOrdenFormSet(request.POST, instance=orden)
#         if orden_form.is_valid() and formset.is_valid():
#             for form in formset:
#                 plato = form.cleaned_data.get('id_carta')
#                 cantidad = form.cleaned_data.get('cantidad')
#                 if plato and cantidad and plato.controlStock == True:
#                     print(plato)
#                     print(cantidad_anterior)
#                     print(plato.controlStock)
#                     print()
#                     for x in range(0, len(cantidad_anterior)):
#                         print(x)
#                         print("uno", str(cantidad_anterior[x]["plato"]) == str(plato))
#                         print("dos", int(cantidad_anterior[x]["cantidad"]) == int(cantidad))
#                         if str(cantidad_anterior[x]["plato"]) == str(plato):
#                             if cantidad_anterior[x]["cantidad"] < cantidad:
#                                 resta= cantidad - cantidad_anterior[x]["cantidad"]
#                                 # Disminuir el stock del plato
#                                 plato.stock -= resta  
#                                 plato.save()  # Guarda los cambios en la base de datos
#                             if cantidad_anterior[x]["cantidad"] > cantidad:
#                                 suma = cantidad_anterior[x]["cantidad"] - cantidad
#                                 plato.stock += suma
#                                 plato.save()  # Guarda los cambios en la base de datos

#                         # if str(cantidad_anterior[x]["plato"]) == str(plato) and cantidad_anterior[x]["cantidad"] != cantidad:


                            
#             formset.instance = orden
#             formset.save()

#             if mesa_anterior != orden.id_mesa:
#                 # Cambiar estado de la mesa original a "libre"
#                 mesa_anterior.estado = False
#                 mesa_anterior.save()
                
#                 # Cambiar estado de la nueva mesa a "ocupado"
#                 mesa = orden.id_mesa
#                 mesa.estado = True
#                 mesa.save()
#             return HttpResponseRedirect(reverse('listaOrdenes'))
#     else:
#         orden_form = OrdenForm(instance=orden)
#         formset = CartaOrdenFormSet(instance=orden)

#     return render(request, "./formularios/formularioOrdenes.html", {
#         'orden_form': orden_form,
#         'formset': formset,
#         "platos":platos,
#         "mesas":mesas,
#     })
# Modificar Orden --------->
def ordenModificar(request, pk):
    orden = Orden.objects.get(id=pk)
    platos = Carta.objects.all()
    mesas = [{"value":x.pk, "text":x.nombre} for x in Mesa.objects.filter(id=orden.id_mesa.pk)]
    mesas_2 = [{"value":x.pk, "text":x.nombre} for x in Mesa.objects.filter(estado=False)]
    mesas.extend(mesas_2)
    mesa_anterior = orden.id_mesa
    cantidad_anterior = [{"plato":x.id_carta, "cantidad":x.cantidad} for x in CartaOrden.objects.filter(id_orden=pk)]
    lista_cant_anterior = [str(diccionario["plato"]) for diccionario in cantidad_anterior ]
    print(lista_cant_anterior)
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST, instance=orden)
        formset = CartaOrdenFormSet(request.POST, instance=orden)
        if orden_form.is_valid() and formset.is_valid():
            orden = orden_form.save()
            for form in formset:
                plato = form.cleaned_data.get('id_carta')
                cantidad = form.cleaned_data.get('cantidad')
                delete = form.cleaned_data.get('DELETE')
                if plato and cantidad and plato.controlStock == True and delete != True:
                    print(plato)
                    print(cantidad_anterior)
                    print(plato.controlStock)
                    print()
                    for x in range(0, len(cantidad_anterior)):
                        print(x)
                        print("uno", str(cantidad_anterior[x]["plato"]) == str(plato))
                        print("dos", int(cantidad_anterior[x]["cantidad"]) == int(cantidad))
                        if str(cantidad_anterior[x]["plato"]) == str(plato):
                            if cantidad_anterior[x]["cantidad"] < cantidad:
                                resta= cantidad - cantidad_anterior[x]["cantidad"]
                                # Disminuir el stock del plato
                                plato.stock -= resta  
                                plato.save()  # Guarda los cambios en la base de datos
                            if cantidad_anterior[x]["cantidad"] > cantidad:
                                suma = cantidad_anterior[x]["cantidad"] - cantidad
                                plato.stock += suma
                                plato.save()  # Guarda los cambios en la base de datos

                    if str(plato) not in lista_cant_anterior:
                        plato.stock -= cantidad  
                        plato.save() 
                        # if str(cantidad_anterior[x]["plato"]) == str(plato) and cantidad_anterior[x]["cantidad"] != cantidad:
                if plato and cantidad and plato.controlStock == True and delete == True:
                    plato.stock += cantidad  
                    plato.save() 


                            
            formset.instance = orden
            formset.save()

            if mesa_anterior != orden.id_mesa:
                # Cambiar estado de la mesa original a "libre"
                mesa_anterior.estado = False
                mesa_anterior.save()
                
                # Cambiar estado de la nueva mesa a "ocupado"
                mesa = orden.id_mesa
                mesa.estado = True
                mesa.save()
            return HttpResponseRedirect(reverse('listaOrdenes'))
    else:
        orden_form = OrdenForm(instance=orden)
        formset = CartaOrdenFormSet(instance=orden)

    return render(request, "./formularios/formularioOrdenes.html", {
        'orden_form': orden_form,
        'formset': formset,
        "platos":platos,
        "mesas":mesas,
    })

# Nueva Orden ------------------>
def ordenNuevo(request):
    platos = Carta.objects.all()
    mesas = [{"value":x.pk, "text":x.nombre} for x in Mesa.objects.filter(estado=False)]
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        formset = CartaOrdenFormSet(request.POST)
        
        if orden_form.is_valid() and formset.is_valid():
            orden = orden_form.save()
            formset.instance = orden
            formset.save()
            for form in formset:# Imprime las claves disponibles
                plato = form.cleaned_data.get('id_carta')
                cantidad = form.cleaned_data.get('cantidad')
                if plato and cantidad and plato.controlStock == True:
                    # Disminuir el stock del plato
                    plato.stock -= cantidad  
                    plato.save()  # Guarda los cambios en la base de datos
                    print(f"plato:{plato.controlStock}")
                    print(f"cantidad:{cantidad}")

            if orden.fecha == orden.fechaModificacion:
                # Actualizar estado de la mesa a "ocupado"
                mesa = orden.id_mesa
                mesa.estado = True
                mesa.save()
            return HttpResponseRedirect(reverse('listaOrdenes'))
    else:
        orden_form = OrdenForm()
        formset = CartaOrdenFormSet()

    return render(request, "./formularios/formularioOrdenes.html", {
        'orden_form': orden_form,
        'formset': formset,
        "platos":platos,
        "mesas":mesas,
    })

# Borrar Orden ----------------------->
def ordenBorrar(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        mesa = orden.id_mesa
        mesa.estado = False
        mesa.save()
        return HttpResponseRedirect(reverse('listaOrdenes'))
    return render(request, './confirmacionBorrado/ordenConfBorrar.html', {'orden': orden})

# FACTURAS VIEWS ---------------------------------------------------------------------------------------------->
# Factura Orden ------->
class listaFacturas(ListView):
    model = Factura
    template_name = "./listas/listafacturas.html"
    context_object_name = 'facturas'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(fecha__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context


# Modificar Factura --------->
# def facturaModificar(request, pk):
#     id_orden_factura = [x.id_orden.pk for x in FacturaOrden.objects.all()]
#     factura_orden = [x.id_orden.pk for x in FacturaOrden.objects.filter(id_factura=pk)]
#     ordenes_select = [{"value":"", "text":"--------" , "total":0}] 
#     ordenes_select.extend([{"value":x.pk, "text":x.id_mesa.nombre + " " + "$"+str(x.total), "total":int(x.total)} for x in Orden.objects.filter(entregado=True) if x.pk in id_orden_factura and x.pk in factura_orden])
#     ordenes_select.extend([{"value":x.pk, "text":x.id_mesa.nombre + " " + "$"+str(x.total), "total":int(x.total)} for x in Orden.objects.filter(entregado=True) if x.pk not in id_orden_factura])
#     ordenes = [x for x in Orden.objects.filter(entregado=True)]
#     factura = Factura.objects.get(id=pk)
#     if request.method == 'POST':
#         factura_form = FacturaForm(request.POST, instance=factura)
#         formset_orden = FacturaOrdenFormSet(request.POST, instance=factura)
#         formset_pago = FacturaPagoFormSet(request.POST, instance=factura)
#         if factura_form.is_valid() and formset_orden.is_valid() and formset_pago.is_valid():
#             factura = factura_form.save()
#             formset_orden.instance = factura
#             formset_orden.save()
#             formset_pago.instance = factura
#             formset_pago.save()
#             #Obtener el valor de los campos
#             #Total de la suma de las ordenes que componen la factura
#             total_factura = factura.total
#             #Total de la suma de la seleccion de los tipos de pago
#             total_pago = factura.total_pago
#             #Total del vuelto que genero la suma de la seleccion de tipos de pago
#             total_vuelto = factura.vuelto
#             print(total_factura)
#             print(total_pago)
#             print(total_vuelto)
#             #Comparamos y en caso de dar con el total de la factura se pone el estado de la factura como "cobrado"
#             if total_factura == total_pago - total_vuelto:
#                 factura.cobrado = True
#                 factura.save()
#             for form in formset_orden:# Imprime las claves disponibles
#                 orden = form.cleaned_data.get('id_orden')
#                 if orden:
#                     orden_id = Orden.objects.get(id=orden.pk)
#                     mesa = orden_id.id_mesa
#                     mesa.estado = False
#                     mesa.save()
#                     # Disminuir el stock del plato
#                     # plato.stock -= cantidad  
#                     # plato.save()  # Guarda los cambios en la base de datos
#                     print(f"orden:{orden.pk}")
#             return HttpResponseRedirect(reverse('listaFacturas'))
#     else:
#         factura_form = FacturaForm(instance=factura)
#         formset_orden = FacturaOrdenFormSet(instance=factura)
#         formset_pago = FacturaPagoFormSet(instance=factura)

#     return render(request, "./formularios/formularioFacturas.html", {
#         'factura_form': factura_form,
#         'formset_orden': formset_orden,
#         'formset_pago': formset_pago,
#         "ordenes_select":ordenes_select,
#         "ordenes":ordenes,
#     })

def facturaModificar(request, pk):
    id_orden_factura = [x.id_orden.pk for x in FacturaOrden.objects.all()]
    factura_orden = [x.id_orden.pk for x in FacturaOrden.objects.filter(id_factura=pk)]
    ordenes_select = [{"value":"", "text":"--------" , "total":0}]
    ordenes_select.extend([{"value":x.pk, "text":x.id_mesa.nombre + " " + "$"+str(x.total), "total":int(x.total)} for x in Orden.objects.filter(entregado=True) if x.pk in id_orden_factura and x.pk in factura_orden])
    ordenes_select.extend([{"value":x.pk, "text":x.id_mesa.nombre + " " + "$"+str(x.total), "total":int(x.total)} for x in Orden.objects.filter(entregado=True) if x.pk not in id_orden_factura])
    ordenes = [x for x in Orden.objects.filter(entregado=True)]
    factura = Factura.objects.get(id=pk)
    
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST, instance=factura)
        formset_orden = FacturaOrdenFormSet(request.POST, instance=factura)
        formset_pago = FacturaPagoFormSet(request.POST, instance=factura)
        
        if factura_form.is_valid() and formset_orden.is_valid() and formset_pago.is_valid():
            # Obtener el valor de los campos
            total_factura = factura.total
            total_pago = factura.total_pago
            total_vuelto = factura.vuelto
            
            # Comprobar si el total pagado es mayor o igual al total de la factura
            if total_pago >= total_factura - total_vuelto:
                factura = factura_form.save()
                formset_orden.instance = factura
                formset_orden.save()
                formset_pago.instance = factura
                formset_pago.save()
                
                # Comprobamos y en caso de dar con el total de la factura se pone el estado de la factura como "cobrado"
                if total_factura == total_pago - total_vuelto:
                    factura.cobrado = True
                    factura.save()

                for form in formset_orden:
                    orden = form.cleaned_data.get('id_orden')
                    if orden:
                        orden_id = Orden.objects.get(id=orden.pk)
                        mesa = orden_id.id_mesa
                        mesa.estado = False
                        mesa.save()
                        print(f"orden:{orden.pk}")
                
                return HttpResponseRedirect(reverse('listaFacturas'))
            else:
                # Esta funcion permite que luego de hacer la comprarcion del total con el total pagado, en caso de no cubrir el total 
                # te muestra un mensaje en el formulario aclarando que solamente puedes proceder si se cumple esta condicion.
                factura_form.add_error(None, "El total pagado debe ser mayor o igual al total de la factura.")
        
    
    else:
        factura_form = FacturaForm(instance=factura)
        formset_orden = FacturaOrdenFormSet(instance=factura)
        formset_pago = FacturaPagoFormSet(instance=factura)
    
    return render(request, "./formularios/formularioFacturas.html", {
        'factura_form': factura_form,
        'formset_orden': formset_orden,
        'formset_pago': formset_pago,
        "ordenes_select": ordenes_select,
        "ordenes": ordenes,
    })

# Nueva Factura ------------------>
def facturaNuevo(request):
    id_orden_factura = [x.id_orden.pk for x in FacturaOrden.objects.all()]
    ordenes_select = [{"value":"", "text":"--------" , "total":0}] 
    ordenes_select.extend([{"value":x.pk, "text":x.id_mesa.nombre + " " + "$"+str(x.total), "total":int(x.total)} for x in Orden.objects.filter(entregado=True) if x.pk not in id_orden_factura])
    ordenes = [x for x in Orden.objects.filter(entregado=True)]
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        formset_orden = FacturaOrdenFormSet(request.POST)
        formset_pago = FacturaPagoFormSet(request.POST)
        if factura_form.is_valid() and formset_orden.is_valid() and formset_pago.is_valid():
            factura = factura_form.save()
            formset_orden.instance = factura
            formset_orden.save()
            formset_pago.instance = factura
            formset_pago.save()
            
            #Obtener el valor de los campos
            #Total de la suma de las ordenes que componen la factura
            total_factura = factura.total
            #Total de la suma de la seleccion de los tipos de pago
            total_pago = factura.total_pago
            #Total del vuelto que genero la suma de la seleccion de tipos de pago
            total_vuelto = factura.vuelto
            print(total_factura)
            print(total_pago)
            print(total_vuelto)
            #Comparamos y en caso de dar con el total de la factura se pone el estado de la factura como "cobrado"
            if total_factura == total_pago - total_vuelto:
                factura.cobrado = True
                factura.save()
            
            for form in formset_orden:# Imprime las claves disponibles
                orden = form.cleaned_data.get('id_orden')
                if orden:
                    orden_id = Orden.objects.get(id=orden.pk)
                    mesa = orden_id.id_mesa
                    mesa.estado = False
                    mesa.save()
                    print(f"orden:{orden.pk}")
                    
            return HttpResponseRedirect(reverse('listaFacturas'))
    else:
        factura_form = FacturaForm()
        formset_orden = FacturaOrdenFormSet()
        formset_pago = FacturaPagoFormSet()

    return render(request, "./formularios/formularioFacturas.html", {
        'factura_form': factura_form,
        'formset_orden': formset_orden,
        'formset_pago': formset_pago,
        "ordenes_select":ordenes_select,
        "ordenes":ordenes,
    })

# Borrar Factura ----------------------->
def facturaBorrar(request, pk):
    factura = Factura.objects.get(id=pk)
    if request.method == 'POST':
        factura.anulado = True
        factura.save()
        return HttpResponseRedirect(reverse('listaFacturas'))
    return render(request, './confirmacionBorrado/facturaConfBorrar.html', {'factura': factura})


# CIERRE VIEWS ----------------------------------------------------------------------------------------->
#Listado Cierres ------------------------------------->
class listaCierres(ListView):
    model = Cierre
    template_name = "./listas/listaCierres.html"
    context_object_name = 'cierres'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(fecha__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context

#Cierre modificar ---------------------------------->
def cierreModif(request, pk):
    cierre = Cierre.objects.get(id=pk)
    if request.method == 'POST':
        form = CierreForm(request.POST, instance=cierre)
        formset = FacturaCierreFormSet(request.POST, instance=cierre)
        if form.is_valid() and formset.is_valid():
            cierre = form.save()
            formset.instance = cierre
            formset.save()
            return HttpResponseRedirect(reverse('listaCierres'))
    else:
        form = CierreForm(instance=cierre)
        formset = FacturaCierreFormSet(instance=cierre)
    return render(request, './formularios/formularioCierre.html', {'form': form, 'formset': formset})

# Nuevo Cierre ------------------>
def cierreNuevo(request):
    lista_id_facturas_en_cierre = [x.id_factura.pk for x in FacturaCierre.objects.all()]
    # Facturas que han sido cobradas y que no han sido anuladas
    facturas = [x for x in Factura.objects.filter(cobrado=True, anulado=False) if x.pk not in lista_id_facturas_en_cierre]
    facturas_js = [{"total":int(x.total), "total_pago":int(x.total_pago), "vuelto":int(x.vuelto)} for x in Factura.objects.filter(cobrado=True, anulado=False) if x.pk not in lista_id_facturas_en_cierre]
    if request.method == 'POST':
        form = CierreForm(request.POST)
        # formset = FacturaCierreFormSet(request.POST)
        
        if form.is_valid():
            cierre = form.save()
            # formset.instance = cierre
            # formset.save()
            print(facturas)
            total , vuelto = 0, 0
            # Itero por cada uno de los diccionarios para usarlos de "instancia"
            for factura in facturas:
                total += factura.total_pago
                vuelto += factura.vuelto
                print(factura.pk)
                print(cierre.pk)
                # Por cada factura genero un nuevo objeto en la tabla intermedia, usando el id del cierre
                FacturaCierre.objects.create(id_cierre=cierre, id_factura=factura)
            cierre.total= total
            cierre.vuelto = vuelto
            cierre.save()
            
            return HttpResponseRedirect(reverse('listaCierres'))
    else:
        form = CierreForm()
        # formset = FacturaCierreFormSet()

    return render(request, "./formularios/formularioCierre.html", {
        'form': form,
        "facturas":facturas,
        "facturas_js":facturas_js,
        
    })

#Cierre borrar ----------------------------------------------->
def cierreBorrar(request, pk):
    cierre = Cierre.objects.get(id=pk)
    if request.method == 'POST':
        cierre.delete()
        return HttpResponseRedirect(reverse('listaCierres'))
    return render(request, './confirmacionBorrado/cierreConfBorrar.html', {'cierre': cierre})

# PLATO DIA VIEWS ----------------------------------------------------------------------------------------->
#Listado Plato día ------------------------------------->
class listaPlatoDia(ListView):
    model = PlatoDia
    template_name = "./listas/listaplatodia.html"
    context_object_name = 'platodia'
    

#Plato dia modificar ---------------------------------->
def PlatoDiaModif(request, pk):
    platoDia = PlatoDia.objects.get(id=pk)
    if request.method == 'POST':
        form = PlatoDiaForm(request.POST, instance=platoDia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaPlatoDia'))
    else:
        form = PlatoDiaForm(instance=platoDia)
    return render(request, './formularios/formularioPlatoDia.html', {'form': form, 'platodia': platoDia})
# Plato día nuevo -------------------------------------------->
def PlatoDiaNuevo(request):
    if request.method == 'POST':
        form = PlatoDiaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaPlatoDia'))
    else:
        form = PlatoDiaForm()
    return render(request, './formularios/formularioPlatoDia.html', {'form': form})
#Plato dia borrar ----------------------------------------------->
def PlatoDiaBorrar(request, pk):
    platoDia = PlatoDia.objects.get(id=pk)
    if request.method == 'POST':
        platoDia.delete()
        return HttpResponseRedirect(reverse('listaPlatoDia'))
    return render(request, './confirmacionBorrado/platoDiaConfBorrar.html', {'platodia': platoDia})

# DETALLES --------------------------------------------------------------------->
#Detalle Carta ----------------->
def cartaDetalle(request, pk):
    carta = Carta.objects.get(id=pk)
    context = {"carta": carta}
    return render(request, "./detalles/cartaDetalle.html", context=context)
#Detalle Mozo ----------------->
def mozoDetalle(request, pk):
    mozo = Mozo.objects.get(id=pk)
    context = {"mozo": mozo}
    return render(request, "./detalles/mozoDetalle.html", context=context)
