"""
URL configuration for Projecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Projecto1.views import saludo, despedida,hora, calculo_edad, curso_C, curso_Css

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),        #Agregamos la Url y la funcion de la view
    path('nosveremos/', despedida),
    path('fecha/', hora),
    path('edades/<int:edad>/<int:anio>', calculo_edad),
    path('cursoC/',curso_C),
    path('cursoCSS/', curso_Css)
]
