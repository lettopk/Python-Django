from django.http import HttpResponse
import datetime
from django.template import Template, Context


##Creando la primer view
def saludo(request):            #Primera vista
    
    doc_externo =  open("C:/Users/marlo/Favorites/python-django/Projecto1/Projecto1/plantillas/plantilla.html")          #llamada del archivo html
    
    plt= Template(doc_externo.read())                                   # se crea objeto template
    doc_externo.close()                                                 #Se cierra documento
    ctx = Context()                                                     # se crea el contexto
    documento = plt.render(ctx)                                         #se renderiza el documento
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse('Adios mundo con django')

def hora(reques):                           ##Llamando contenido dinamico
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actual: %s
    </h2>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calculo_edad(request, edad, anio):      ##Enviando parametros por la url
    periodo = anio - 2025
    edad_futura = edad + periodo
    documento = "<html><body><h2> En el año %s tendras %s años</h2></body></html>" %(anio , edad_futura)
    return HttpResponse(documento)