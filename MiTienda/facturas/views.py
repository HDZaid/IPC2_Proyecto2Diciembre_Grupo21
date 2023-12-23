from django.shortcuts import render

# Create your views here.

def facturas_view(request):
    return render(request, 'facturas.html')