from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="paginaPrincipal"),
    path("bebidas/", views.listaBebidas, name="listaBebidas"),
    path("platos/", views.listaPlatos, name="listaPlatos"),
    path("postres/", views.listaPostres, name="listaPostres"),
    path("mesas/", views.listaMesas, name="listaMesas"),
    path("clientes/", views.listaClientes, name="listaClientes"),
    
]
