from django.shortcuts import render
from .models import Cliente, Producto 
# Create your views here.

def facturas_view(request):
    return render(request, 'facturas.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'clientes.html')

def productos_view(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'productos.html')