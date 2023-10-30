from django.contrib import admin
from .models import Reserva

# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    #form = ReservaForm
    list_display = ('Ejemplar','Estudiante','Fecha_reserva','Fecha_reserva_vencida','Estado')


admin.site.register(Reserva, ReservaAdmin)