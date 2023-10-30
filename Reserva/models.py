from django.db import models
from Estudiante.models import Estudiante
from Ejemplar.models import Ejemplar
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    Ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Cantidad_dias = models.SmallIntegerField('Cantidad de dias en llevarse el ejemplar', default = 10)
    Fecha_reserva = models.DateField('Fecha de creación de reserva: ', auto_now_add = False)
    Fecha_reserva_vencida = models.DateField('Fecha de vencimiento de la reserva: ', null = True, blank = True)
    Estado = models.BooleanField(default=True, verbose_name='Estado')

    def save(self, *args, **kwargs):
        if self.Fecha_reserva >= self.Fecha_reserva_vencida:
            raise ValueError('La fecha de creación debe ser anterior a la fecha de vencimiento')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'

    def __str__(self):
        return f'Reserva de libros {self.Ejemplar} por el estudiante {self.Estudiante}'   

@receiver(post_save, sender = Reserva)

def AgregarFechaVencidaReserva(sender, instance, **kwargs):
    if not instance.Fecha_reserva_vencida:
        instance.Fecha_reserva_vencida = instance.Fecha_reserva + timedelta(days=instance.Cantidad_dias)
        instance.save()