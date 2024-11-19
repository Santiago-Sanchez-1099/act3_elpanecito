from django.db import models
class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=11)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(10, 2)
    fecha_ingreso = models.DateField()
    id_categoria = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre_producto