from django.contrib import admin
from facturas.models import Cliente, Producto
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dpi', 'nit', 'nombre')
    search_fields = ['nombre']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'cantidad')
    search_fields = ['nombre']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
admin.site.register(Producto, ProductoAdmin)