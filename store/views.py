from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def lista_clientes(request):
    return render(request, 'clientes/lista_clientes.html')

def cliente_by_id(request):
    return render(request, 'clientes/cliente.html')