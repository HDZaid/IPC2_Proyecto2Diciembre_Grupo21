from django.urls import path
from.import views
urlpatterns = [
    path('', views.facturas_view, name='Facturas'),
    path('clientes/', views.clientes_view, name='Clientes'),
]