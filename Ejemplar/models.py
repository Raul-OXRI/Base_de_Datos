from django.db import models
from Biblioteca.models import Biblioteca
from .choices import Formato
# Create your models here.

class Ejemplar(models.Model):
    id = models.AutoField(primary_key=True)
    Imagen = models.ImageField()
    Titulo = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    Año = models.IntegerField()
    Editorial = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=11, choices=Formato)
    Existencia = models.IntegerField()
    Biblioteca = models.ManyToManyField(Biblioteca,blank=True,)
    
    class Meta:
        verbose_name='ejemplar'
        verbose_name_plural='ejemplar'

    def __str__(self):
        return self.Titulo