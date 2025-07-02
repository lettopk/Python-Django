from django.db import models

#Se crea una clase por cada tabla  que necesite el proyecto

class clientes (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La Direccion")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    
class articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    def __str__(self):                              #llamado de cadena de caracteres
        return self.nombre

class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()