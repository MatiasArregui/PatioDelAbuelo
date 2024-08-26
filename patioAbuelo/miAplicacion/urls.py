from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="paginaPrincipal"),
    path("bebidas/", views.listaBebidas, name="listaBebidas"),
    path('bebidas/bebidaNueva/', views.bebidaNuevo, name='bebidaNueva'),
    path('bebidas/bebidaModif/<int:pk>/', views.bebidaModificar, name='bebidaModif'),
    path('bebidas/bebidaBorrar/<int:pk>/', views.bebidaBorrar, name='bebidaBorrar'),
    
    
    
    
    
    path("platos/", views.listaPlatos, name="listaPlatos"),
    path("postres/", views.listaPostres, name="listaPostres"),
    path("mesas/", views.listaMesas, name="listaMesas"),
    path("clientes/", views.listaClientes, name="listaClientes"),
    
    path("ordenes/", views.listaOrdenes, name="listaOrdenes"),
    
]
