from django.db import models

# Create your models here.
class Catalogo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
