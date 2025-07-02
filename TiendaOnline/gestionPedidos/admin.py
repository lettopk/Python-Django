from django.contrib import admin
from gestionPedidos.models import clientes, articulos, pedidos

class clientes_admin (admin.ModelAdmin):
    list_display = ("nombre","direccion","telefono")
    search_fields = ("nombre","telefono")

class articulos_admin (admin.ModelAdmin):
    list_display = ("nombre","seccion","precio")
    list_filter = ("seccion",)
    
class pedidos_admin(admin.ModelAdmin):
    list_display = ("numero","fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"
    
    
admin.site.register(clientes,clientes_admin)
admin.site.register(articulos,articulos_admin)
admin.site.register(pedidos,pedidos_admin)

