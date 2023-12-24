from django.db import models
from django.utils import timezone
# Create your models here.

#codigo = DPI


class Cliente(models.Model):
    dpi = models.CharField(max_length=15, unique=True, null=False, blank=False)
    nit = models.CharField(max_length=8, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, unique=True, null=False, blank=False)
    direccion = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        verbose_name='clientes'
        verbose_name_plural='clientes'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=200, unique=True, null=False, blank=False)
    precio = models.CharField(max_length=100, unique=True, null=False, blank=False)
    cantidad = models.CharField(max_length=200, unique=True, null=False, blank=False)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        order_with_respect_to = 'descripcion'
    
    def __str__(self):
        return self.descripcion
