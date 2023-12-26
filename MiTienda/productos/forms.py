from django import forms
from productos.models import Clientes, Producto


class AddClienteForm(forms.ModelForm):
    
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono' )
        labels = {
            'codigo' : 'Codigo Clientes: ',
            'nombre' : 'Nombre Cliente: ',
            'telefono' : 'Telefono Cliente: ',
            
        }
        
class EditarClienteForm(forms.ModelForm):
    
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono' )
        labels = {
            'codigo' : 'Codigo Clientes: ',
            'nombre' : 'Nombre Cliente: ',
            'telefono' : 'Telefono Cliente: ',
            
        }
        widgets = {
            'codigo' : forms.TextInput(attrs={'type' : 'text', 'id' : 'codigo_editar' }),
            'nombre' : forms.TextInput(attrs={'id' :  'nombre_editar' }),
            'telefono' : forms.TextInput(attrs={'id' :  'telefono_editar' }),
        }
        
class AddProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion', 'costo', 'precio', 'cantidad' )
        labels = {
            'codigo' : 'Codigo: ',
            'descripcion ' : 'Descipcion de producto: ',
            'costo' : 'costo: ',
            'precio' : 'Precio: ',
            'cantidad' : 'Cantidad: ',
            
        }
        