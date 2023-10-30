from django.db import models
from Estudiante.models import Estudiante
from Ejemplar.models import Ejemplar
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

class Prestamo(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    Ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Cantidad_dias = models.SmallIntegerField('Cantidad de Dias a Reservar',default = 10)
    Fecha_creacion = models.DateField('Fecha de creación', auto_now_add = True)
    Fecha_vencida = models.DateField('Fecha de vencimiento de la reserva', null = True, blank = True)
    Estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'prestamo'
        verbose_name_plural = 'prestamos'

    def __str__(self):
        return f'Reserva de libros {self.Ejemplar} por el estudiante {self.Estudiante}'   

@receiver(post_save, sender = Prestamo)

def AgregarFechaVencidaPrestamo(sender, instance, **kwargs):
    if not instance.Fecha_vencida:
        instance.Fecha_vencida = instance.Fecha_creacion + timedelta(days=instance.Cantidad_dias)
        instance.save()