from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos

# Create your views here.
#Vista para el formulario
def busqueda_producto(request):
    return render(request, "busqueda_productos.html")

#vista para la busqueda
def buscar(request):
    if request.GET["producto"]:
        #mensaje ="Aeticulo buscado: %r" %request.GET["producto"]
        producto_encontrado = request.GET["producto"]
        articulos_encontrados = articulos.objects.filter(nombre__icontains = producto_encontrado)   #busqueda "SQL" en la tabla
        return render(request, "resultados_busqueda.html", {"articulos_encontrados":articulos_encontrados, "query":producto_encontrado})
    
    else:
        mensaje ="No has introducido nada" 
          
    return HttpResponse(mensaje)