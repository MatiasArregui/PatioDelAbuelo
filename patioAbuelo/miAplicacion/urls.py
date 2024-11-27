from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Login ----------------------------------------------------------------------------------->
    path('', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'),
    
    #Pagina de inicio ------------------------------------------------------------------------>
    path("inicio/", login_required(login_required(views.principal)), name="paginaPrincipal"),
   
    
    #Ordenes -------------------------------------------------------------------------------->
    path("ordenes/", login_required(views.listaOrdenes.as_view()), name="listaOrdenes"),
    path("ordenes/ordenNueva/", login_required(views.ordenNuevo), name="ordenNueva"),
    path("ordenes/ordenModif/<int:pk>/", login_required(views.ordenModificar), name="ordenModificar"),
    path("ordenes/ordenBorrar/<int:pk>/", login_required(views.ordenBorrar), name="ordenBorrar"),
    
    #Facturas -------------------------------------------------------------------------------->
    path("facturas/", login_required(views.listaFacturas.as_view()), name="listaFacturas"),
    path("facturas/facturaNueva/", login_required(views.facturaNuevo), name="facturaNueva"),
    path("facturas/facturaModif/<int:pk>/", login_required(views.facturaModificar), name="facturaModificar"),
    path("facturas/facturaBorrar/<int:pk>/", login_required(views.facturaBorrar), name="facturaBorrar"),
    
    #clientes -------------------------------------------------------------------------------->
    path("clientes/", login_required(views.listaClientes.as_view()), name="listaClientes"),
    path("clientes/clienteNuevo/", login_required(views.ClienteNuevo), name="clienteNuevo"),
    path("clientes/clienteModif/<int:pk>/", login_required(views.ClienteModif), name="clienteModificar"),
    path("clientes/clienteBorrar/<int:pk>/", login_required(views.ClienteBorrar), name="clienteBorrar"),

    #Mesas ------------------------------------------------------------------------------------->
    path("mesas/", login_required(views.listaMesas.as_view()), name="listaMesas"),
    path('mesas/mesaNueva/', login_required(views.mesaNueva), name='mesaNueva'),
    path('mesas/mesaModif/<int:pk>/', login_required(views.mesaModificar), name='mesaModif'),
    path('mesas/mesaBorrar/<int:pk>/', login_required(views.mesaBorrar), name='mesaBorrar'),
    
    #Carta ---------------------------------------------------------------------------------->
    path("carta/", login_required(views.listaCarta.as_view()), name="listaCarta"),
    path('carta/cartaNuevo/', login_required(views.cartaNuevo), name='cartaNuevo'),
    path('carta/cartaModif/<int:pk>/', login_required(views.cartaModificar), name='cartaModif'),
    path('carta/cartaBorrar/<int:pk>/', login_required(views.cartaBorrar), name='cartaBorrar'),
    
    #Mozos ---------------------------------------------------------------------------------->
    path("mozos/", login_required(views.listaMozos.as_view()), name="listaMozos"),
    path('mozos/mozoNuevo/', login_required(views.MozoNuevo), name='mozoNuevo'),
    path('mozos/mozoModif/<int:pk>/', login_required(views.MozoModif), name='mozoModif'),
    path('mozos/mozoBorrar/<int:pk>/', login_required(views.MozoBorrar), name='mozoBorrar'),
    
    #Cierre ---------------------------------------------------------------------------------->
    path("cierre/", login_required(views.listaCierres.as_view()), name="listaCierres"),
    path('cierre/cierreNuevo/', login_required(views.cierreNuevo), name='cierreNuevo'),
    path('cierre/cierreModif/<int:pk>/', login_required(views.cierreModif), name='cierreModif'),
    path('cierre/cierreBorrar/<int:pk>/', login_required(views.cierreBorrar), name='cierreBorrar'),
    
    

    #Plato del día ---------------------------------------------------------------------------------->
    path("platodia/", login_required(views.listaPlatoDia.as_view()), name="listaPlatoDia"),
    path('platodia/platoDiaNuevo/', login_required(views.PlatoDiaNuevo), name='platoDiaNuevo'),
    path('platodia/platoDiaModif/<int:pk>/', login_required(views.PlatoDiaModif), name='platoDiaModif'),
    path('platodia/platoDiaBorrar/<int:pk>/', login_required(views.PlatoDiaBorrar), name='platoDiaBorrar'),

    # DETALLES ------------------------------------------------->
    path("carta/<int:pk>", login_required(views.cartaDetalle), name="cartaDetalle"),
    path("mozos/<int:pk>", login_required(views.mozoDetalle), name="mozoDetalle"),
    path("clientes/<int:pk>", login_required(views.clienteDetalle), name="clienteDetalle"),
    path("mesas/<int:pk>", login_required(views.mesaDetalle), name="mesaDetalle"),
    path("cierre/<int:pk>", login_required(views.cierreDetalle), name="cierreDetalle"),
    path("ordenes/<int:pk>", login_required(views.ordenDetalle), name="ordenDetalle"),
    
    
]
