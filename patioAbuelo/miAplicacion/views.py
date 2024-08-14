from django.shortcuts import render
from .models import Bebida, Plato, Postre, Cliente, Mesa, Orden, Factura

# Create your views here.
def principal(request):
    return render(request, template_name="base.html")
