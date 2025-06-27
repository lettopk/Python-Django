from django.http import HttpResponse

##Creando la primer view
def saludo(request):            #Primera vista
    return HttpResponse("Hola mundo con django!")


def despedida(request):
    return HttpResponse('Adios mundo con django')