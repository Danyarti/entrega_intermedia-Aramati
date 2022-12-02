from django.shortcuts import render

from .models import *

def cliente (request):
    return render ("Mercado_Fino/cliente.html")

def producto (request):
    return render ("Mercado_Fino/producto.html")

def vendedor (request):
    return render ("Mercado_Fino/vendedor.html")

# Create your views here.
