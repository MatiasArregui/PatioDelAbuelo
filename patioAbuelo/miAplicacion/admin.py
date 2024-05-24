from django.contrib import admin
from .models import Plato, PlatoOrden, Orden, Mesa, Factura, Cliente
# Register your models here.
admin.site.register(Plato)
admin.site.register(Mesa)
admin.site.register(Cliente)
# admin.site.register(Factura)

class DetalleInline(admin.TabularInline):
    model = PlatoOrden


class OrdenAdmin(admin.ModelAdmin):
    inlines = [
        DetalleInline,
    ]
admin.site.register(Orden, OrdenAdmin)

class OrdenInline(admin.TabularInline):
    model = Orden


class FacturaAdmin(admin.ModelAdmin):
    inlines = [
        OrdenInline,
    ]
admin.site.register(Factura, FacturaAdmin)
