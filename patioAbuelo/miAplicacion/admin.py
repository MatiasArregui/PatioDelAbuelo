from django.contrib import admin
from .models import Carta, CartaOrden, Factura, FacturaOrden, Mozo, Mesa, Cliente, Categoria, SubCategoria, Orden, TipoPago, FacturaPago, Cierre, FacturaCierre
# Register your models here.
admin.site.register(Mesa)
admin.site.register(TipoPago)

# DETALLES DE cATEGORIAS -------------------------------------->
class CategoriaDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre")
    
admin.site.register(Categoria, CategoriaDetalle)

# DETALLES DE SUBCATEGORIAS -------------------------------------->
class SubcategoriasDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre")
    
admin.site.register(SubCategoria, SubcategoriasDetalle)

# DETALLES DE MOZO -------------------------------------->
class MozoDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "telefono")
    
admin.site.register(Mozo, MozoDetalle)

# DETALLES DE CARTA -------------------------------------->
class CartaDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "controlStock", "stock", "categoria", "subCategoria")
    
admin.site.register(Carta, CartaDetalle)

# DETALLES DE CLIENTE -------------------------------------->
class ClienteDetalle(admin.ModelAdmin):
    list_display = ("id", "nombre", "telefono")

admin.site.register(Cliente, ClienteDetalle)


# INLINES DE ORDEN Y FACTURA ----------------------------------------->

# INLINE DETALLE DE ORDEN ---------------------------->
class OrdenDetalleInline(admin.TabularInline):
    model = CartaOrden

class OrdenAdmin(admin.ModelAdmin):
    inlines = [
        OrdenDetalleInline,
    ]
    list_display = ("id", "id_mesa", "fecha", "fechaModificacion")
    
admin.site.register(Orden, OrdenAdmin)

# INLINE DETALLE DE FACTURA ---------------------------->    
class OrdenInline(admin.TabularInline):
    model = FacturaOrden
    
# INLINE TIPO DE FACTURA ---------------------------->    
class TipoInline(admin.TabularInline):
    model = FacturaPago
    list_display = ("id", "pago", "total")

class FacturaAdmin(admin.ModelAdmin):
    inlines = [
        OrdenInline,
        TipoInline,
    ]
    list_display = ("id", "fecha", "total")

admin.site.register(Factura, FacturaAdmin)

# INLINE CIERRE DE FACTURA ---------------------------->    
class FacturaInline(admin.TabularInline):
    model = FacturaCierre

class CierreAdmin(admin.ModelAdmin):
    inlines = [
        FacturaInline,
    ]

admin.site.register(Cierre, CierreAdmin)
