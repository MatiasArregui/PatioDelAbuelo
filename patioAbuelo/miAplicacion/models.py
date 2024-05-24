from django.db import models

# Create your models here.


# MODELO DE PLATO ------------------------------------>
class Plato(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre + " " + str(self.precio)
    
# MODELO DE MESA -----------------------------------------> 
class Mesa(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nombre   

# MODELO DE CLIENTE ----------------------------------------->
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nombre

# MODELO FACTURA ----------------------------------------------->
class Factura(models.Model):
    Id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    Total = models.IntegerField()
    
    def __str__(self) -> str:
        return self.Id_cliente.nombre + " " + str(self.fecha)

# MODELO DE ORDEN ----------------------------------------->
class Orden(models.Model):
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, default=None, blank=True, null=True)
    id_plato = models.ManyToManyField(Plato, through="PlatoOrden")
    total = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.pk) + " " + self.id_mesa.nombre + " " + str(self.total) 
    

    
# MODELO DE PLATO_ORDEN ----------------------------------------->
class PlatoOrden(models.Model):
    id_plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pk)
    