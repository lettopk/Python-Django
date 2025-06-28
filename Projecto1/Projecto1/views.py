from django.http import HttpResponse
import datetime
#from django.template import Template, Context
#from django.template.loader import get_template
from django.shortcuts import render

class persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

##Creando la primer view

def saludo(request):            #Primera vista
    p1 = persona("Marlon" , "Tarazona")                                         #se crea el objeto persona para mostrar

    temas_curso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]  #Lista para mostrar

    ahora = datetime.datetime.now()                                             #variable simple con llamado de datetime
                #(request, "nombre_plantilla", contexto)                        Prametros de render
    return render(request, 'plantilla.html', {"nombre_persona":p1.nombre,
                   "apellido_persona":p1.apellido, 
                   "hora_actual": ahora, 
                   "temas":temas_curso})
    
    """
      #Metodo basico para llamar y crrear una plantilla_________________________________________________________________________________________________________________________
        
            doc_externo =  open("C:/Users/marlo/Favorites/python-django/Projecto1/Projecto1/plantillas/plantilla.html")  #llamada del archivo html, carga la plantilla
                                                                                #Se envia la ruta a "DIRS" en setting.py
            plt= Template(doc_externo.read())                                   # se crea objeto template
            doc_externo.close()                                                 #Se cierra documento
            
            ctx = Context({"nombre_persona":p1.nombre,
                           "apellido_persona":p1.apellido, 
                           "hora_actual": ahora, 
                           "temas":temas_curso})                            # se crea el contexto, donde se puede agregar un diccionario con la variable a mostrar
            
            documento = plt.render(ctx)
            return #HttpResponse(documento)
        
      #Metodo rapido de cargado de plantillas___________________________________________________________________________________________________________________________________   
            doc_externo = get_template('plantilla.html')     #Se utiliza el cargador de plantillas
            documento = doc_externo.render({"nombre_persona":p1.nombre,
                           "apellido_persona":p1.apellido, 
                           "hora_actual": ahora, 
                           "temas":temas_curso})                                         #se renderiza el documento
            
            Simplificacion de codigo con shortcuts____________________________________________________________________________________________________________________________
            return HttpResponse(documento)
"""

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