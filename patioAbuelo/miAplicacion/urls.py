from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="paginaPrincipal"),
    
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
    
    #clientes -------------------------------------------------------------------------------->
    path("clientes/", views.listaClientes, name="listaClientes"),
    path("clientes/clienteNueva/", views.clientesNuevo, name="clienteNueva"),
    path("clientes/clienteModif/<int:pk>/", views.clientesModificar, name="clienteModificar"),
    path("clientes/clienteBorrar/<int:pk>/", views.clientesBorrar, name="clienteBorrar"),
    
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
    
    
    
    path("platos/", views.listaPlatos, name="listaPlatos"),

    
    

    
]
