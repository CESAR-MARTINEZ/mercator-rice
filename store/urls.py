
from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes),
    path('clientes/id', views.cliente_by_id)
]
