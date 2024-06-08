from django.contrib import admin
from .models import Plato, PlatoOrden, Orden, Mesa, Factura, Cliente, FacturaOrden, Bebida, Postre, BebidaOrden, PostreOrden
# Register your models here.
admin.site.register(Mesa)

# DETALLES DE BEBIDA -------------------------------------->
class BebidaDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "cantidad")
    
admin.site.register(Bebida, BebidaDetalle)

# DETALLES DE POSTRE -------------------------------------->
class PostreDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "cantidad")
    
admin.site.register(Postre, PostreDetalle)

# DETALLES DE PLATO -------------------------------------->
class PlatoDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio")
    
admin.site.register(Plato, PlatoDetalle)

# DETALLES DE CLIENTE -------------------------------------->
class ClienteDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "telefono")

admin.site.register(Cliente, ClienteDetalle)


# INLINES DE ORDEN Y FACTURA ----------------------------------------->

# INLINE DETALLE DE ORDEN ---------------------------->
class OrdenDetalleInline(admin.TabularInline):
    model = PlatoOrden

class PostreDetalleInline(admin.TabularInline):
    model = PostreOrden
    
class BebidaDetalleInline(admin.TabularInline):
    model = BebidaOrden

class OrdenAdmin(admin.ModelAdmin):
    inlines = [
        OrdenDetalleInline,
        BebidaDetalleInline,
        PostreDetalleInline
    ]
    list_display = ("id", "id_mesa")
    
admin.site.register(Orden, OrdenAdmin)

# INLINE DETALLE DE FACTURA ---------------------------->    
class OrdenInline(admin.TabularInline):
    model = FacturaOrden

class FacturaAdmin(admin.ModelAdmin):
    inlines = [
        OrdenInline,
    ]
    list_display = ("id", "fecha", "Total")

admin.site.register(Factura, FacturaAdmin)

