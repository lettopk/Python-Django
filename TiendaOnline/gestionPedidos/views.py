from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from gestionPedidos.models import articulos
from django.conf import settings
from gestionPedidos.forms import formulario_contacto

# Create your views here.
#Vista para el formulario
def busqueda_producto(request):
    return render(request, "busqueda_productos.html")

#vista para la busqueda
def buscar(request):
    if request.GET["producto"]:
        #mensaje ="Aeticulo buscado: %r" %request.GET["producto"]
        producto_a_buscar = request.GET["producto"]
        if len(producto_a_buscar)>20:           #limitamos a 20 caractres el producto a buscar   
            mensaje = "Texto de busqueda demasiado largo"
        else:    
            articulos_encontrados = articulos.objects.filter(nombre__icontains = producto_a_buscar)   #busqueda "SQL" en la tabla
            return render(request, "resultados_busqueda.html", {"articulos_encontrados":articulos_encontrados, "query":producto_a_buscar})
    
    else:
        mensaje ="No has introducido nada" 
          
    return HttpResponse(mensaje)


def contacto(request):
    if request.method=="POST":
        
        mi_formulario = formulario_contacto(request.POST)                   #Guardamos aqui el formulario
        if mi_formulario.is_valid():                                        #Verifica si el formulario es valido
            inf_form = mi_formulario.cleaned_data                           #Guardamos la los datos introducidos en el formulario
            send_mail(inf_form['asunto'],                                   #Desde aqui se envia el correo con los datos del formulario
                      inf_form['mensaje'],
                      inf_form.get('email',''),
                      ['mtarazona97@uan.edu.co'])
            
            return render(request,'gracias.html')
    else:
        mi_formulario = formulario_contacto()                               #Se crea el formulario vacio
    
    return render(request, "formulario_contacto.html",{"form":mi_formulario})#Se renderiza el formulario vacio
            
""" Formulario Manual
        subject = request.POST["asunto"]                                    #Aqui se rescata el asunto introducido en el formulario
        message = request.POST["mensaje"] + " de:" + request.POST["email"]  #Aqui se rescata el mensaje y el email introducido en el formulario
        email_from = settings.EMAIL_HOST_USER                               #De donde se envia el correo
        recipient_list = ["mtarazona97@uan.edu.co"]                         #Donde llega el correo
        send_mail(subject,message,email_from,recipient_list)                #Instruccion para armar el correo y enviar
        
        
        return render(request,'gracias.html')                               #Vista hacia el cliente

return render(request,'contacto.html')"""