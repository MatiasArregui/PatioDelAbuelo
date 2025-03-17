from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # Login ----------------------------------------------------------------------------------->
    path('', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'),
    
    # Página de inicio ------------------------------------------------------------------------>
    path("inicio/", login_required(views.principal), name="paginaPrincipal"),
    
    # Página de QR------------------------------------------------------------------------>
    path("home/", views.landingPage, name="landingPage"),
    
    # Órdenes --------------------------------------------------------------------------------->
    path("ordenes/", login_required(permission_required('miAplicacion.view_orden')(views.listaOrdenes.as_view())), name="listaOrdenes"),
    path("ordenes/ordenNueva/", login_required(permission_required('miAplicacion.add_orden')(views.ordenNuevo)), name="ordenNueva"),
    path("ordenes/ordenModif/<int:pk>/", login_required(permission_required('miAplicacion.change_orden')(views.ordenModificar)), name="ordenModificar"),
    path("ordenes/ordenBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_orden')(views.ordenBorrar)), name="ordenBorrar"),
    
    # Facturas -------------------------------------------------------------------------------->
    path("facturas/", login_required(permission_required('miAplicacion.view_factura')(views.listaFacturas.as_view())), name="listaFacturas"),
    path("facturas/facturaNueva/", login_required(permission_required('miAplicacion.add_factura')(views.facturaNuevo)), name="facturaNueva"),
    path("facturas/facturaModif/<int:pk>/", login_required(permission_required('miAplicacion.change_factura')(views.facturaModificar)), name="facturaModif"),
    path("facturas/facturaBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_factura')(views.facturaBorrar)), name="facturaBorrar"),
    
    # Clientes -------------------------------------------------------------------------------->
    path("clientes/", login_required(permission_required('miAplicacion.view_cliente')(views.listaClientes.as_view())), name="listaClientes"),
    path("clientes/clienteNuevo/", login_required(permission_required('miAplicacion.add_cliente')(views.ClienteNuevo)), name="clienteNuevo"),
    path("clientes/clienteModif/<int:pk>/", login_required(permission_required('miAplicacion.change_cliente')(views.ClienteModif)), name="clienteModificar"),
    path("clientes/clienteBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_cliente')(views.ClienteBorrar)), name="clienteBorrar"),
    
    # Mesas ----------------------------------------------------------------------------------->
    path("mesas/", login_required(permission_required('miAplicacion.view_mesa')(views.listaMesas.as_view())), name="listaMesas"),
    path("mesas/mesaNueva/", login_required(permission_required('miAplicacion.add_mesa')(views.mesaNueva)), name="mesaNueva"),
    path("mesas/mesaModif/<int:pk>/", login_required(permission_required('miAplicacion.change_mesa')(views.mesaModificar)), name="mesaModif"),
    path("mesas/mesaBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_mesa')(views.mesaBorrar)), name="mesaBorrar"),
    
    # Carta ----------------------------------------------------------------------------------->
    path("carta/", login_required(permission_required('miAplicacion.view_carta')(views.listaCarta.as_view())), name="listaCarta"),
    path("carta/cartaNuevo/", login_required(permission_required('miAplicacion.add_carta')(views.cartaNuevo)), name="cartaNuevo"),
    path("carta/cartaModif/<int:pk>/", login_required(permission_required('miAplicacion.change_carta')(views.cartaModificar)), name="cartaModif"),
    path("carta/cartaBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_carta')(views.cartaBorrar)), name="cartaBorrar"),
    
    # Mozos ----------------------------------------------------------------------------------->
    path("mozos/", login_required(permission_required('miAplicacion.view_mozo')(views.listaMozos.as_view())), name="listaMozos"),
    path("mozos/mozoNuevo/", login_required(permission_required('miAplicacion.add_mozo')(views.MozoNuevo)), name="mozoNuevo"),
    path("mozos/mozoModif/<int:pk>/", login_required(permission_required('miAplicacion.change_mozo')(views.MozoModif)), name="mozoModif"),
    path("mozos/mozoBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_mozo')(views.MozoBorrar)), name="mozoBorrar"),
    
    # Cierre ---------------------------------------------------------------------------------->
    path("cierre/", login_required(permission_required('miAplicacion.view_cierre')(views.listaCierres.as_view())), name="listaCierres"),
    path("cierre/cierreNuevo/", login_required(permission_required('miAplicacion.add_cierre')(views.cierreNuevo)), name="cierreNuevo"),
    
    # Plato del Día --------------------------------------------------------------------------->
    path("platodia/", login_required(permission_required('miAplicacion.view_platodia')(views.listaPlatoDia.as_view())), name="listaPlatoDia"),
    path("platodia/platoDiaNuevo/", login_required(permission_required('miAplicacion.add_platodia')(views.PlatoDiaNuevo)), name="platoDiaNuevo"),
    path("platodia/platoDiaModif/<int:pk>/", login_required(permission_required('miAplicacion.change_platodia')(views.PlatoDiaModif)), name="platoDiaModif"),
    path("platodia/platoDiaBorrar/<int:pk>/", login_required(permission_required('miAplicacion.delete_platodia')(views.PlatoDiaBorrar)), name="platoDiaBorrar"),
    
    # Detalles -------------------------------------------------------------------------------->
    path("carta/<int:pk>", login_required(permission_required('miAplicacion.view_carta')(views.cartaDetalle)), name="cartaDetalle"),
    path("facturas/<int:pk>", login_required(permission_required('miAplicacion.view_factura')(views.facturaDetalle)), name="facturaDetalle"),
    path("ordenes/<int:pk>", login_required(permission_required('miAplicacion.view_orden')(views.ordenDetalle)), name="ordenDetalle"),
    path("cierre/<int:pk>", login_required(permission_required('miAplicacion.view_cierre')(views.cierreDetalle)), name="cierreDetalle"),
]

