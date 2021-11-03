from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    nombreProducto = models.CharField(max_length=100,
                                      verbose_name="Nombre del producto")
    stockInicial = models.PositiveIntegerField(blank=True,
                                               verbose_name= "Cantidad "
                                                             "inicial")
    stockActual = models.PositiveIntegerField(blank=True,
                                              verbose_name="Cantidad "
                                                           "disponible")
    precio = models.PositiveIntegerField(verbose_name="Precio de Compra")
    estado = models.BooleanField()

    class Meta:
        verbose_name= "Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombreProducto