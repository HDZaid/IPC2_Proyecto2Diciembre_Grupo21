from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo = models.CharField(max_length = 200, null = True, blank = True)
    nombre = models.CharField(max_length = 200, null = True, blank = False)
    telefono = models.CharField(max_length = 200, null = True, blank = False)
    created = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField( auto_now_add=True)
    
    class Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'
        
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length = 200, unique = True, null = True, blank = True)
    descripcion = models.CharField(max_length = 300, unique = True, null = False)
    # imagen = models.ImageField(upload_to='productos', null = True, blank =True )
    costo = models.DecimalField(max_digits = 18, decimal_places = 2, null = False)
    precio = models.DecimalField(max_digits = 18, decimal_places = 2, null = False, default = 0, blank = True )
    cantidad = models.DecimalField(max_digits = 15, decimal_places = 2, null = False)
    created = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField( auto_now_add=True)
    
    class Meta:
        verbose_name = 'productos'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'
        
        
    def __str__(self):
        return self.descripcion
    
    
    
    