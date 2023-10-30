from django.contrib import admin
from .models import Prestamo

# Register your models here.
class PrestamoAdmin(admin.ModelAdmin):
    #form = ReservaForm
    list_display = ('Ejemplar','Estudiante','Fecha_creacion','Fecha_vencida','Estado')


admin.site.register(Prestamo, PrestamoAdmin)