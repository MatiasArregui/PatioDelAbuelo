from django.db import models

# Create your models here.
# MODELO DE CATEGORIA ------------------------------------>
class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.nombre
    
# MODELO DE SUBCATEGORIA ------------------------------------>
class SubCategoria(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.nombre
    
# MODELO DE CARTA ------------------------------------>
class Carta(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    controlStock = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes/')
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre + " " + str(self.precio)
    

# MODELO DE MESA -----------------------------------------> 
class Mesa(models.Model):
    nombre = models.CharField(max_length=120)
    estado = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.nombre

# MODELO DE CLIENTE ----------------------------------------->
class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre
    
# MODELO DE MOZO ----------------------------------------->
class Mozo(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre
    
# MODELO DE TIPO PAGO ----------------------------------------->
class TipoPago(models.Model):
    pago = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.pago

# MODELO FACTURA ----------------------------------------------->
class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    total_pago = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vuelto = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    anulado = models.BooleanField(default=False)
    cobrado = models.BooleanField(default=False)
    #Este set default elije al cliente cuyo id sea 3 (consumidor final) para llenar el espacio
    # del cliente eliminado
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_orden = models.ManyToManyField("Orden", through="FacturaOrden")
    id_tipoPago = models.ManyToManyField(TipoPago, through="FacturaPago")
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.id_cliente.nombre + " " + str(self.fecha)

# MODELO DE ORDEN ----------------------------------------->
class Orden(models.Model):
    total = models.DecimalField(max_digits=15, decimal_places=2)
    observacion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    entregado = models.BooleanField(default=False)
    facturado = models.BooleanField(default=False)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)
    id_carta = models.ManyToManyField(Carta, through="CartaOrden")
    id_mozo = models.ForeignKey(Mozo, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.id_mesa.nombre + " " + str(self.total) 
    
# MODELO DE MOZO ----------------------------------------->
class Cierre(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total_ordenes = models.DecimalField(max_digits=15, decimal_places=2)
    total_facturas = models.DecimalField(max_digits=15, decimal_places=2)
    vuelto = models.DecimalField(max_digits=15, decimal_places=2)
    id_factura = models.ManyToManyField(Factura, through="FacturaCierre")
    
    def __str__(self) -> str:
        return str(self.pk)
    
    
# MODELO DE CARTA_ORDEN ----------------------------------------->
class CartaOrden(models.Model):
    id_carta = models.ForeignKey(Carta, on_delete=models.PROTECT)
    id_orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.pk)

# MODELO DE FACTURA_ORDEN ----------------------------------------->
class FacturaOrden(models.Model):
    id_orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    id_factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return str(self.pk)
    
# MODELO DE FACTURA_PAGO ----------------------------------------->
class FacturaPago(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    id_tipoPago = models.ForeignKey(TipoPago, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    

    def __str__(self) -> str:
        return str(self.pk)
    
# MODELO DE FACTURA_CIERRE ----------------------------------------->
class FacturaCierre(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    id_cierre = models.ForeignKey(Cierre, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return str(self.pk)
    
# MODELO DE PLATO DEL DIA----------------------------------------->
class PlatoDia(models.Model):
    id_carta = models.ForeignKey(Carta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pk)