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
        if self.controlStock:
            return self.nombre + " " + f"Categoria: {self.subCategoria.nombre}"
        else:
            return self.nombre
    

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
def seleccionar_cliente_alternativo():
    # Buscamos el mozo comun o base que remplazara a los demas
    cliente_alternativo = Cliente.objects.filter(nombre__exact="Consumidor final").first()
    if cliente_alternativo:
        return cliente_alternativo
    
class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    total_pago = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vuelto = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    anulado = models.BooleanField(default=False)
    cobrado = models.BooleanField(default=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    id_orden = models.ManyToManyField("Orden", through="FacturaOrden")
    id_tipoPago = models.ManyToManyField(TipoPago, through="FacturaPago")
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.id_cliente.nombre + " " + str(self.fecha)

# MODELO DE ORDEN ----------------------------------------->
# Función para seleccionar otro mozo
def seleccionar_mozo_alternativo():
    # Buscamos el mozo comun o base que remplazara a los demas
    mozo_alternativo = Mozo.objects.filter(nombre__exact="Mozo").first()
    if mozo_alternativo:
        return mozo_alternativo
    
def seleccionar_mesa_alternativa():
    # Buscamos el mozo comun o base que remplazara a los demas
    mesa_alternativa = Mesa.objects.filter(nombre__exact="Mesa predeterminada").first()
    if mesa_alternativa:
        return mesa_alternativa
    

class Orden(models.Model):
    total = models.DecimalField(max_digits=15, decimal_places=2)
    observacion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    entregado = models.BooleanField(default=False)
    facturado = models.BooleanField(default=False)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.SET(seleccionar_mesa_alternativa))
    id_carta = models.ManyToManyField(Carta, through="CartaOrden")
    id_mozo = models.ForeignKey(
        'Mozo',
        on_delete=models.SET(seleccionar_mozo_alternativo)  # Cambiado a SET con función personalizada
    )
    
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
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
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