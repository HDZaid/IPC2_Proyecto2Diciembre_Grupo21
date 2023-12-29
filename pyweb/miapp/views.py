from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Factura, DetalleFactura
from .forms import ProductoForm, ClienteForm, FacturaForm, DetalleFacturaForm
from django.db.models import Q

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/detalle_producto.html', {'producto': producto})

def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto/nuevo_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'producto/eliminar_producto.html', {'producto': producto})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

def nuevo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'cliente/nuevo_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        cliente.delete()
        return redirect('lista_clientes')

    return render(request, 'cliente/eliminar_cliente.html', {'cliente': cliente})

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/lista_facturas.html', {'facturas': facturas})

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = DetalleFactura.objects.filter(factura=factura)

    total_factura = sum(detalle.subtotal for detalle in detalles)

    return render(request, 'factura/detalle_factura.html', {'factura': factura, 'detalles': detalles, 'total_factura': total_factura})

def crear_factura(request):
    if request.method == "POST":
        factura_form = FacturaForm(request.POST)
        detalle_form = DetalleFacturaForm(request.POST)

        if factura_form.is_valid() and detalle_form.is_valid():
            factura = factura_form.save(commit=False)

            cliente_id = request.POST.get('cliente')
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            factura.cliente = cliente
            factura.save()

            
            detalle = detalle_form.save(commit=False)
            detalle.factura = factura
            detalle.save()

            return redirect('detalle_factura', pk=factura.pk)
    else:
        factura_form = FacturaForm()
        detalle_form = DetalleFacturaForm()

    return render(request, 'factura/crear_factura.html', {'factura_form': factura_form, 'detalle_form': detalle_form})

def editar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = DetalleFactura.objects.filter(factura=factura)

    if request.method == "POST":
        detalle_form = DetalleFacturaForm(request.POST)

        if detalle_form.is_valid():
            
            factura_detalle = detalles.first()  
            factura_detalle.producto = detalle_form.cleaned_data['producto']
            factura_detalle.cantidad = detalle_form.cleaned_data['cantidad']
            factura_detalle.save()

            return redirect('detalle_factura', pk=factura.pk)
    else:
        
        detalle_form = DetalleFacturaForm(initial={'producto': detalles.first().producto,
                                                   'cantidad': detalles.first().cantidad})

    return render(request, 'factura/editar_factura.html', {'factura': factura, 'detalle_form': detalle_form})


def eliminar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)

    if request.method == "POST":
        factura.delete()
        return redirect('lista_facturas')

    return render(request, 'factura/eliminar_factura.html', {'factura': factura})


def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            
            productos = Producto.objects.filter(
                Q(nombre__icontains=query) | Q(descripcion__icontains=query)
            )

            clientes = Cliente.objects.filter(
                Q(nombre__icontains=query) | Q(direccion__icontains=query)
            )

            facturas = Factura.objects.filter(
                Q(cliente__nit__icontains=query)
            )

            return render(request, 'buscar/buscar.html', {'productos': productos, 'clientes': clientes, 'facturas': facturas, 'query': query})
    
    return render(request, 'buscar/buscar.html')  

# miapp
def pagina_inicio(request):
    return render(request, 'menu/pagina_inicio.html')
