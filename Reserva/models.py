from django.db import models
from Estudiante.models import Estudiante
from Ejemplar.models import Ejemplar

# Create your models here.
class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    Ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Cantidad_dias = models.IntegerField('Cantida de dias a reservar', default=10)
    Fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    Fecha_vencida = models.DateField('Fecha de vencimiento de reserva', auto_now= False, auto_now_add=True, blank=True)
    Estado = models.BooleanField(default=True, verbose_name='Estado')
    
    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'
    
    def __str__(self):
        return f'Reserva de libros {self.Ejemplar} por el estudiante {self.Estudiante}'
