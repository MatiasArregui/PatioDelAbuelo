from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Login ----------------------------------------------------------------------------------->
    path("", views.loginIngreso, name="loginIngreso"),
    
    #Pagina de inicio ------------------------------------------------------------------------>
    path("inicio/", views.principal, name="paginaPrincipal"),
    
    #Bebidas -------------------------------------------------------------------------------->
    path("bebidas/", views.listaBebidas, name="listaBebidas"),
    path('bebidas/bebidaNueva/', views.bebidaNuevo, name='bebidaNueva'),
    path('bebidas/bebidaModif/<int:pk>/', views.bebidaModificar, name='bebidaModif'),
    path('bebidas/bebidaBorrar/<int:pk>/', views.bebidaBorrar, name='bebidaBorrar'),
    
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
    
    #Postres ---------------------------------------------------------------------------------->
    path("postres/", views.listaPostre, name="listaPostres"),
    path('postres/postreNuevo/', views.postreNuevo, name='postreNuevo'),
    path('postres/postreModif/<int:pk>/', views.postreModificar, name='postreModif'),
    path('postres/postreBorrar/<int:pk>/', views.postreBorrar, name='postreBorrar'),

    #Mesas ------------------------------------------------------------------------------------->
    path("mesas/", views.listaMesas, name="listaMesas"),
    path('mesas/mesaNueva/', views.mesaNueva, name='mesaNueva'),
    path('mesas/mesaModif/<int:pk>/', views.mesaModificar, name='mesaModif'),
    path('mesas/mesaBorrar/<int:pk>/', views.mesaBorrar, name='mesaBorrar'),
    
    #Platos ---------------------------------------------------------------------------------->
    path("platos/", views.listaPlato, name="listaPlatos"),
    path('platos/platoNuevo/', views.platoNuevo, name='platoNuevo'),
    path('platos/platoModif/<int:pk>/', views.platoModificar, name='platoModif'),
    path('platos/platoBorrar/<int:pk>/', views.platoBorrar, name='platoBorrar'),
    
    #Mozos ---------------------------------------------------------------------------------->
    path("mozos/", views.listaMozos, name="listaMozos"),
    path('mozos/mozoNuevo/', views.MozoNuevo, name='mozoNuevo'),
    path('mozos/mozoModif/<int:pk>/', views.MozoModif, name='mozoModif'),
    path('mozos/mozoBorrar/<int:pk>/', views.MozoBorrar, name='mozoBorrar'),
    
    
]
