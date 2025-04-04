from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Orden, Carta, Factura, Cliente, Mesa, Mozo, SubCategoria, Categoria, CartaOrden, FacturaOrden, Cierre, FacturaCierre, PlatoDia
from .forms import MozoForm, ClienteForm, CartaForm, OrdenForm, CartaOrdenFormSet, FacturaForm, FacturaOrdenFormSet, FacturaPagoFormSet, CierreForm,  FacturaCierreFormSet, LoginForm, PlatoDiaForm, MesaForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView
import random
import os
# from datetime import datetime, timedelta
# import pytz

# Pagina principal ----------------------------------------------------------------------------------->
def principal(request):
    cartaId = [x.pk for x in Carta.objects.all()]
    carta_aleratoria = random.choice(cartaId)
    carta = Carta.objects.get(id=carta_aleratoria)
    try: 
        platoDia = PlatoDia.objects.get()
        context = {"carta": carta,
               "platoDia":platoDia}
    except:
        context = {"carta": carta,
               "platoDia":{}}
    return render(request, template_name="paginaPrincipal.html", context=context)

# Login de ingreso ------------------------------------------------------------------------------------->
class LoginIngreso(LoginView):
    template_name = os.path.join("registration", "login.html")
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("paginaPrincipal")


# PLATO VIEWS ------------------------------------------------------------------------------>
# Listado plato --------------------------->
class listaCarta(ListView):
    model = Carta
    template_name = os.path.join("listas", "listaCarta.html")
    context_object_name = 'carta'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subCategorias = SubCategoria.objects.all()
        # Aquí agrego otro contexto, para filtar en el template
        context['subcategorias'] = subCategorias
        context['query'] = self.request.GET.get('q', '')  
        print(context)
        return context
        

# Modificar plato ------------->
def cartaModificar(request, pk):
    carta = Carta.objects.get(id=pk)
    # Filtramos las categorias existentes y de esta forma mandamos estas estructuras de datos al js
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
    return render(request, os.path.join("formularios", "formularioCarta.html"), {'form': form, 'carta': carta, "opcion1":opcion1, "opcion2":opcion2, "opcion3":opcion3, "categorias":categorias})

# Nuevo plato ------------------>
def cartaNuevo(request):
    # Filtramos las categorias existentes y de esta forma mandamos estas estructuras de datos al js
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
    return render(request, os.path.join("formularios", "formularioCarta.html"), {'form': form, "opcion1":opcion1, "opcion2":opcion2, "opcion3":opcion3, "categorias":categorias})

# Borrar plato ----------------------->
def cartaBorrar(request, pk):
    # carta = Carta.objects.get(id=pk)
    carta= get_object_or_404(Carta, id=pk)
    
    if request.method == 'POST':
        try: 
            carta.delete()
            return HttpResponseRedirect(reverse('listaCarta'))
        except ProtectedError:
            messages.error(request, "No se puede eliminar el plato porque tiene ordenes relacionadas. Se recomienda volver atras")
    return render(request, os.path.join("confirmacionBorrado", "cartaConfBorrar.html"), {'carta': carta})

# MESAS VIEWS ----------------------------------->
# Listado Mesa ------->
class listaMesas(ListView):
    model = Mesa
    template_name = os.path.join("listas", "listaMesas.html")
    context_object_name = 'mesas'

# Modificar Mesa --------->
def mesaModificar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMesas'))
    else:
        form = MesaForm(instance=mesa)
    return render(request, os.path.join("formularios", "formularioMesas.html"),  {'form': form, 'mesa': mesa})

# Nueva Mesa --------->
def mesaNueva(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMesas'))
    else:
        form = MesaForm()
    return render(request, os.path.join("formularios", "formularioMesas.html"), {'form': form})

# Borrar Mesa ----------------------->
def mesaBorrar(request, pk):
    mesa = Mesa.objects.get(id=pk)
    if request.method == 'POST':
        try: 
            mesa.delete()
            return HttpResponseRedirect(reverse('listaMesas'))
        except ProtectedError:
            messages.error(request, "No se puede eliminar la mesa porque tiene ordenes relacionadas. Se recomienda volver atras")
        
    return render(request, os.path.join("confirmacionBorrado", "mesaConfBorrar.html"), {'mesa': mesa})

# CIENTES VIEWS ---------------------------------------------------------------------------------------------->
# Listado Cliente -------
class listaClientes(ListView):
    model = Cliente
    template_name = os.path.join("listas", "listaClientes.html")
    context_object_name = 'clientes'
    paginate_by = 12
    
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
    return render(request, os.path.join("formularios", "formularioClientes.html"), {'form': form, 'cliente': cliente})

# Nuevo Cliente ------------------>
def ClienteNuevo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaClientes'))
    else:
        form = ClienteForm()
    return render(request, os.path.join("formularios", "formularioClientes.html"), {'form': form})

# Borrar Cliente ----------------------->
def ClienteBorrar(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        try: 
            cliente.delete()
            return HttpResponseRedirect(reverse('listaClientes'))
        except ProtectedError:
            messages.error(request, "No se puede eliminar el cliente porque tiene facturas relacionadas. Se recomienda volver atras")
    return render(request, os.path.join("confirmacionBorrado", "clienteConfBorrar.html"), {'cliente': cliente})

# MOZO VIEWS ----------------------------------------------------------------------------------------->
#Listado Mozos ------------------------------------->
class listaMozos(ListView):
    model = Mozo
    template_name = os.path.join("listas", "listaMozos.html")
    context_object_name = 'mozos'
    

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
    return render(request, os.path.join("formularios", "formularioMozos.html"), {'form': form, 'mozo': mozo})
# Mozo nuevo -------------------------------------------->
def MozoNuevo(request):
    if request.method == 'POST':
        form = MozoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaMozos'))
    else:
        form = MozoForm()
    return render(request, os.path.join("formularios", "formularioMozos.html"), {'form': form})
#Mozo borrar ----------------------------------------------->
def MozoBorrar(request, pk):
    mozo = Mozo.objects.get(id=pk)
    if request.method == 'POST':
        try: 
            mozo.delete()
            return HttpResponseRedirect(reverse('listaMozos'))
        except ProtectedError:
            messages.error(request, "No se puede eliminar el mozo porque tiene ordenes relacionadas. Se recomienda volver atras")
    return render(request, os.path.join("confirmacionBorrado", "mozoConfBorrar.html"), {'mozo': mozo})

# ORDEN VIEWS ---------------------------------------------------------------------------------------------->
# Listado Orden ------->
class listaOrdenes(ListView):
    model = Orden
    template_name = os.path.join("listas", "listaOrdenes.html")
    context_object_name = 'ordenes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro', 'todas')  

        if filtro == 'entregadas':
            queryset = queryset.filter(entregado=True)  
        elif filtro == 'no_entregadas':
            queryset = queryset.filter(entregado=False)  
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = self.request.GET.get('filtro', 'todas')
        # Agregamos contextos que seran utilizados en el template
        context['cartaOrden'] = [{"id":x.pk, "id_carta":x.id_carta, "id_orden":x.id_orden, "cantidad":x.cantidad} for x in CartaOrden.objects.all()]
        context["facturaOrden"] = [x.id_orden.pk for x in FacturaOrden.objects.all()]
        return context

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
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST, instance=orden)
        formset = CartaOrdenFormSet(request.POST, instance=orden)
        if orden_form.is_valid() and formset.is_valid():
            orden = orden_form.save()
            for form in formset:
                # Aca obtenemos el dato de cada uno de los inputs en formato diccionario
                plato = form.cleaned_data.get('id_carta')
                cantidad = form.cleaned_data.get('cantidad')
                delete = form.cleaned_data.get('DELETE')
                # En este if siguiente se resta el stock
                if plato and cantidad and plato.controlStock == True and delete != True:
                    for x in range(0, len(cantidad_anterior)):
                        if str(cantidad_anterior[x]["plato"]) == str(plato):
                            if cantidad_anterior[x]["cantidad"] < cantidad:
                                resta= cantidad - cantidad_anterior[x]["cantidad"]
                                # Disminuir el stock del plato
                                plato.stock -= resta  
                                # Guardamos los cambios
                                plato.save()  
                            if cantidad_anterior[x]["cantidad"] > cantidad:
                                suma = cantidad_anterior[x]["cantidad"] - cantidad
                                plato.stock += suma
                                plato.save()  
                    # Se resta stock si el plato se agrego en esta modificacion
                    if str(plato) not in lista_cant_anterior:
                        plato.stock -= cantidad  
                        plato.save() 
                # Este if restablece el stock si se ha seleccionado el eliminar en el formulario
                if plato and cantidad and plato.controlStock == True and delete == True:
                    plato.stock += cantidad  
                    plato.save() 
                            
            formset.instance = orden
            formset.save()

            if mesa_anterior != orden.id_mesa:
                # Cambiar estado de la mesa original a "desocupado"
                mesa_anterior.estado = False
                mesa_anterior.save()
                
                # Cambiar estado de la mesa a "ocupado"
                mesa = orden.id_mesa
                mesa.estado = True
                mesa.save()
            return HttpResponseRedirect(reverse('listaOrdenes'))
    else:
        orden_form = OrdenForm(instance=orden)
        formset = CartaOrdenFormSet(instance=orden)

    return render(request,os.path.join("formularios", "formularioOrdenes.html"), {
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
            for form in formset:
                plato = form.cleaned_data.get('id_carta')
                cantidad = form.cleaned_data.get('cantidad')
                if plato and cantidad and plato.controlStock == True:
                    # Disminuir el stock del plato
                    plato.stock -= cantidad  
                    plato.save() 
                    print(f"plato:{plato.controlStock}")
                    print(f"cantidad:{cantidad}")

            if orden.fecha == orden.fechaModificacion:
                # Actualizamos el estado de la mesa a "ocupado"
                mesa = orden.id_mesa
                mesa.estado = True
                mesa.save()
            return HttpResponseRedirect(reverse('listaOrdenes'))
    else:
        orden_form = OrdenForm()
        formset = CartaOrdenFormSet()

    return render(request,os.path.join("formularios", "formularioOrdenes.html"), {
        'orden_form': orden_form,
        'formset': formset,
        "platos":platos,
        "mesas":mesas,
    })

# Borrar Orden ----------------------->
def ordenBorrar(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        try: 
            orden.delete()
            mesa = orden.id_mesa
            mesa.estado = False
            mesa.save()
            return HttpResponseRedirect(reverse('listaOrdenes'))
        except ProtectedError:
            messages.error(request, "No se puede eliminar la orden porque tiene facturas relacionadas. Se recomienda volver atras")

    return render(request, os.path.join("confirmacionBorrado", "ordenConfBorrar.html"), {'orden': orden})

# FACTURAS VIEWS ---------------------------------------------------------------------------------------------->
# Factura lista ------->
class listaFacturas(ListView):
    model = Factura
    template_name = os.path.join("listas", "listaFacturas.html")
    context_object_name = 'facturas'
    paginate_by = 12

    def get_queryset(self):
         # Ordenar por fecha descendente
        queryset = super().get_queryset().order_by('-fecha') 
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(fecha__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        context['facturaCierre'] = [x.id_factura.pk for x in FacturaCierre.objects.all()]
        return context


# Modificar Factura --------->
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
    
    return render(request, os.path.join("formularios", "formularioFacturas.html"), {
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
            #Comparamos y en caso de dar con el total de la factura se pone el estado de la factura como "cobrado"
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
                    
            return HttpResponseRedirect(reverse('listaFacturas'))
    else:
        factura_form = FacturaForm()
        formset_orden = FacturaOrdenFormSet()
        formset_pago = FacturaPagoFormSet()

    return render(request, os.path.join("formularios", "formularioFacturas.html"), {
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
    return render(request, os.path.join("confirmacionBorrado", "facturaConfBorrar.html"), {'factura': factura})


# CIERRE VIEWS ----------------------------------------------------------------------------------------->
#Listado Cierres ------------------------------------->
class listaCierres(ListView):
    model = Cierre
    template_name = os.path.join("listas", "listaCierres.html")
    context_object_name = 'cierres'
    paginate_by = 10
    
    def get_queryset(self):
        # los ordeno por la fecha mas reciente
        queryset = super().get_queryset().order_by('-fecha')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(fecha__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '') 
        return context


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

    return render(request, os.path.join("formularios", "formularioCierre.html"), {
        'form': form,
        "facturas":facturas,
        "facturas_js":facturas_js,
        
    })

# PLATO DIA VIEWS ----------------------------------------------------------------------------------------->
#Listado Plato día ------------------------------------->
class listaPlatoDia(ListView):
    model = PlatoDia
    template_name = os.path.join("listas", "listaPlatoDia.html")
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
    return render(request,os.path.join("formularios", "formularioPlatoDia.html"), {'form': form, 'platodia': platoDia})
# Plato día nuevo -------------------------------------------->
def PlatoDiaNuevo(request):
    if request.method == 'POST':
        form = PlatoDiaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaPlatoDia'))
    else:
        form = PlatoDiaForm()
    return render(request, os.path.join("formularios", "formularioPlatoDia.html"), {'form': form})
#Plato dia borrar ----------------------------------------------->
def PlatoDiaBorrar(request, pk):
    platoDia = PlatoDia.objects.get(id=pk)
    if request.method == 'POST':
        platoDia.delete()
        return HttpResponseRedirect(reverse('listaPlatoDia'))
    return render(request, os.path.join("confirmacionBorrado", "platoDiaConfBorrar.html"), {'platodia': platoDia})

# DETALLES --------------------------------------------------------------------->
#Detalle Carta ----------------->
def cartaDetalle(request, pk):
    carta = Carta.objects.get(id=pk)
    context = {"carta": carta}
    return render(request, os.path.join("detalles", "cartaDetalle.html"), context=context)

#Detalle Cierre ----------------->
def cierreDetalle(request, pk):
    cierre = Cierre.objects.get(id=pk)
    facturaCierreId = [x.id_factura.pk for x in FacturaCierre.objects.filter(id_cierre=cierre.pk)]
    facturas = [x for x in Factura.objects.all() if x.pk in facturaCierreId]
    context = {"cierre": cierre, "facturas":facturas}
    return render(request, os.path.join("detalles", "cierreDetalle.html"), context=context)

#Detalle Orden ----------------->
def ordenDetalle(request, pk):
    orden = Orden.objects.get(id=pk)
    facturaOrdenId = [x.id_carta.pk for x in CartaOrden.objects.filter(id_orden=orden.pk)]
    carta = [x for x in Carta.objects.all() if x.pk in facturaOrdenId]
    context = {"orden": orden, "carta":carta}
    return render(request, os.path.join("detalles", "ordenDetalle.html"), context=context)

#Detalle Factura ----------------->
def facturaDetalle(request, pk):
    factura = Factura.objects.get(id=pk)
    facturaOrdenes = [x.id_orden.pk for x in FacturaOrden.objects.filter(id_factura=pk)]
    ordenes = [x for x in Orden.objects.all() if x.pk in facturaOrdenes]
    datos_ordenes = []
    for orden in ordenes:
        platosId = [x.id_carta.pk for x in CartaOrden.objects.filter(id_orden=orden.pk)]
        platos = [{"nombre": x.id_carta.nombre, "precio":x.id_carta.precio, "cantidad":x.cantidad} for x in CartaOrden.objects.filter(id_orden=orden.pk)]
        datos_ordenes.append({"orden":orden, "platos":platos})
    context= {"factura":factura, "datos_ordenes": datos_ordenes}
    return render(request, os.path.join("detalles", "facturaDetalle.html"), context=context)

# Landing Page ----------------------------------------------------------------------------------->
def landingPage(request):
    try: 
        platoDia = PlatoDia.objects.get()
        context = {"platoDia":platoDia}
    except:
        context = {"platoDia":{}}
    return render(request, template_name="landingPage.html", context=context)
    