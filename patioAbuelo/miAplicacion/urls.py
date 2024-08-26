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
    path("postre/", views.listaPostre, name="listaPostre"),
    path('postre/postreNuevo/', views.postreNuevo, name='postreNuevo'),
    path('postre/postreModif/<int:pk>/', views.postreModificar, name='postreModif'),
    path('postre/postreBorrar/<int:pk>/', views.postreBorrar, name='postreBorrar'),

    path("mesas/", views.listaMesas, name="listaMesas"),
    path("clientes/", views.listaClientes, name="listaClientes"),
    
]
