from django.shortcuts import render
from .models import *
# Create your views here.


def CargarIndex(request):
    return render(request, "pages/index.html")

def Cargarperros(request):
    return render(request, "pages/perros.html")

def Cargargatos(request):
    return render(request, "pages/gatos.html")

def Cargarlogin(request):
    return render(request, "pages/login.html")

def Cargarproductos(request):
    productos = Producto.objects.filter(stock__gt = "0").order_by("nombre")
    categorias = Categoria.objects.all()
    return render(request, "pages/productos.html",{"productos":productos,"categoria":categorias})


def CargarArt_aseo(request):
    return render(request, "pages/art_aseo.html")