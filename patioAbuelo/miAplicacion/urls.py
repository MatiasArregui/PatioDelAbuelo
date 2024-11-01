from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Login ----------------------------------------------------------------------------------->
    path("", views.loginIngreso, name="loginIngreso"),
    
    #Pagina de inicio ------------------------------------------------------------------------>
    path("inicio/", views.principal, name="paginaPrincipal"),
    
    #Ordenes -------------------------------------------------------------------------------->
    path("ordenes/", views.listaOrdenes, name="listaOrdenes"),
    path("ordenes/ordenNueva/", views.ordenNuevo, name="ordenNueva"),
    path("ordenes/ordenModif/<int:pk>/", views.ordenModificar, name="ordenModificar"),
    path("ordenes/ordenBorrar/<int:pk>/", views.ordenBorrar, name="ordenBorrar"),
    
    #Facturas -------------------------------------------------------------------------------->
    path("facturas/", views.listaFacturas, name="listaFacturas"),
    path("facturas/facturaNueva/", views.facturaNuevo, name="facturaNueva"),
    path("facturas/facturaModif/<int:pk>/", views.facturaModificar, name="facturaModificar"),
    path("facturas/facturaBorrar/<int:pk>/", views.facturaBorrar, name="facturaBorrar"),
    
    #clientes -------------------------------------------------------------------------------->
    path("clientes/", views.listaClientes, name="listaClientes"),
    path("clientes/clienteNuevo/", views.ClienteNuevo, name="clienteNuevo"),
    path("clientes/clienteModif/<int:pk>/", views.ClienteModif, name="clienteModificar"),
    path("clientes/clienteBorrar/<int:pk>/", views.ClienteBorrar, name="clienteBorrar"),

    #Mesas ------------------------------------------------------------------------------------->
    path("mesas/", views.listaMesas, name="listaMesas"),
    path('mesas/mesaNueva/', views.mesaNueva, name='mesaNueva'),
    path('mesas/mesaModif/<int:pk>/', views.mesaModificar, name='mesaModif'),
    path('mesas/mesaBorrar/<int:pk>/', views.mesaBorrar, name='mesaBorrar'),
    
    #Carta ---------------------------------------------------------------------------------->
    path("carta/", views.listaCarta, name="listaCarta"),
    path('carta/cartaNuevo/', views.cartaNuevo, name='cartaNuevo'),
    path('carta/cartaModif/<int:pk>/', views.cartaModificar, name='cartaModif'),
    path('carta/cartaBorrar/<int:pk>/', views.cartaBorrar, name='cartaBorrar'),
    
    #Mozos ---------------------------------------------------------------------------------->
    path("mozos/", views.listaMozos, name="listaMozos"),
    path('mozos/mozoNuevo/', views.MozoNuevo, name='mozoNuevo'),
    path('mozos/mozoModif/<int:pk>/', views.MozoModif, name='mozoModif'),
    path('mozos/mozoBorrar/<int:pk>/', views.MozoBorrar, name='mozoBorrar'),
    
    #Cierre ---------------------------------------------------------------------------------->
    path("cierre/", views.listaCierres, name="listaCierres"),
    path('cierre/cierreNuevo/', views.cierreNuevo, name='cierreNuevo'),
    path('cierre/cierreModif/<int:pk>/', views.cierreModif, name='cierreModif'),
    path('cierre/cierreBorrar/<int:pk>/', views.cierreBorrar, name='cierreBorrar'),
    
    
]
