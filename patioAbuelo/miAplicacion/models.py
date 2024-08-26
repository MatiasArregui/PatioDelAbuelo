from django.db import models

# Create your models here.
# MODELO DE PLATO ------------------------------------>
class Plato(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self) -> str:
        return self.nombre + " " + str(self.precio)
    
# MODELO DE BEBIDAS ------------------------------------>
class Bebida(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre + " " + str(self.precio)
    
# MODELO DE BEBIDAS ------------------------------------>
class Postre(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    
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

# MODELO FACTURA ----------------------------------------------->
class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=15, decimal_places=2)
    Id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_orden = models.ManyToManyField("Orden", through="FacturaOrden")
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.Id_cliente.nombre + " " + str(self.fecha)

# MODELO DE ORDEN ----------------------------------------->
class Orden(models.Model):
    total = models.DecimalField(max_digits=15, decimal_places=2)
    observacion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    id_plato = models.ManyToManyField(Plato, through="PlatoOrden")
    id_postre = models.ManyToManyField(Postre, through="PostreOrden")
    id_bebida = models.ManyToManyField(Bebida, through="BebidaOrden")
 

    def __str__(self) -> str:
        return str(self.pk) + " " + self.id_mesa.nombre + " " + str(self.total) 
    
    
# MODELO DE PLATO_ORDEN ----------------------------------------->
class PlatoOrden(models.Model):
    id_plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.pk)

# MODELO DE POSTRE_ORDEN ----------------------------------------->
class PostreOrden(models.Model):
    id_postre = models.ForeignKey(Postre, on_delete=models.CASCADE)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.pk)
    
# MODELO DE BEBIDA_ORDEN ----------------------------------------->
class BebidaOrden(models.Model):
    id_bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.pk)

# MODELO DE FACTURA_ORDEN ----------------------------------------->
class FacturaOrden(models.Model):
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.pk)
    
    