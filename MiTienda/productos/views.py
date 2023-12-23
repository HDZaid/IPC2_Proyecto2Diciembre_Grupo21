from django.shortcuts import render

# Create your views here.

def productos_view(request):
    return render(request, 'productos.html')