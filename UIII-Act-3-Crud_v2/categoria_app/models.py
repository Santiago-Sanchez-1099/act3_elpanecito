from django.db import models
class Categoria(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=11)
    nombre_categoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    fecha_creacion = models.DateField()
    id_usuario = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre_categoria