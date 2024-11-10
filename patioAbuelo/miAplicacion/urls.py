from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .forms import LoginForm

urlpatterns = [
    #Login ----------------------------------------------------------------------------------->
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'),
    
    #Pagina de inicio ------------------------------------------------------------------------>
    path("inicio/", views.principal, name="paginaPrincipal"),
    
    #Ordenes -------------------------------------------------------------------------------->
    path("ordenes/", views.listaOrdenes.as_view(), name="listaOrdenes"),
    path("ordenes/ordenNueva/", views.ordenNuevo, name="ordenNueva"),
    path("ordenes/ordenModif/<int:pk>/", views.ordenModificar, name="ordenModificar"),
    path("ordenes/ordenBorrar/<int:pk>/", views.ordenBorrar, name="ordenBorrar"),
    
    #Facturas -------------------------------------------------------------------------------->
    path("facturas/", views.listaFacturas.as_view(), name="listaFacturas"),
    path("facturas/facturaNueva/", views.facturaNuevo, name="facturaNueva"),
    path("facturas/facturaModif/<int:pk>/", views.facturaModificar, name="facturaModificar"),
    path("facturas/facturaBorrar/<int:pk>/", views.facturaBorrar, name="facturaBorrar"),
    
    #clientes -------------------------------------------------------------------------------->
    path("clientes/", views.listaClientes.as_view(), name="listaClientes"),
    path("clientes/clienteNuevo/", views.ClienteNuevo, name="clienteNuevo"),
    path("clientes/clienteModif/<int:pk>/", views.ClienteModif, name="clienteModificar"),
    path("clientes/clienteBorrar/<int:pk>/", views.ClienteBorrar, name="clienteBorrar"),

    #Mesas ------------------------------------------------------------------------------------->
    path("mesas/", views.listaMesas.as_view(), name="listaMesas"),
    path('mesas/mesaNueva/', views.mesaNueva, name='mesaNueva'),
    path('mesas/mesaModif/<int:pk>/', views.mesaModificar, name='mesaModif'),
    path('mesas/mesaBorrar/<int:pk>/', views.mesaBorrar, name='mesaBorrar'),
    
    #Carta ---------------------------------------------------------------------------------->
    path("carta/", views.listaCarta.as_view(), name="listaCarta"),
    path('carta/cartaNuevo/', views.cartaNuevo, name='cartaNuevo'),
    path('carta/cartaModif/<int:pk>/', views.cartaModificar, name='cartaModif'),
    path('carta/cartaBorrar/<int:pk>/', views.cartaBorrar, name='cartaBorrar'),
    
    #Mozos ---------------------------------------------------------------------------------->
    path("mozos/", views.listaMozos.as_view(), name="listaMozos"),
    path('mozos/mozoNuevo/', views.MozoNuevo, name='mozoNuevo'),
    path('mozos/mozoModif/<int:pk>/', views.MozoModif, name='mozoModif'),
    path('mozos/mozoBorrar/<int:pk>/', views.MozoBorrar, name='mozoBorrar'),
    
    #Cierre ---------------------------------------------------------------------------------->
    path("cierre/", views.listaCierres.as_view(), name="listaCierres"),
    path('cierre/cierreNuevo/', views.cierreNuevo, name='cierreNuevo'),
    path('cierre/cierreModif/<int:pk>/', views.cierreModif, name='cierreModif'),
    path('cierre/cierreBorrar/<int:pk>/', views.cierreBorrar, name='cierreBorrar'),
    
    
]
