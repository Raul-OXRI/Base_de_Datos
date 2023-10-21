from django.db import models
from .choices import Region
from django.core.validators import RegexValidator


class Encargado(models.Model):
    id_encargado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=13,default='+502 ',help_text='El número de teléfono debe tener 8 dígitos,sin espacios.',)
    Correo_electronico = models.EmailField()
    Contrasena = models.CharField(max_length=100)
    #Created = models.DateTimeField(auto_now_add=True)
    #Updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='encargado'
        verbose_name_plural='encargados'
    
    def __str__(self):
        return self.Nombre

class Biblioteca(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Ubicacion = models.CharField(max_length=50)
    Region = models.CharField(max_length=13, choices=Region)
    Horario = models.CharField(max_length=50)
    Encargado = models.ForeignKey(Encargado, null=True,blank=True, on_delete=models.SET_NULL)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='biblioteca'
        verbose_name_plural='bibliotecas'

    def __str__(self):
        return self.Nombre
    
