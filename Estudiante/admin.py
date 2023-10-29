from django.contrib import admin
from .models import Estudiante

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Carrera', 'Correo_electronico')

admin.site.register(Estudiante, EstudianteAdmin)


#def get_biblioteca(obj):
#    return ', '.join([biblioteca.Nombre for biblioteca in obj.Biblioteca.all()])

#admin.site.register(Ejemplar, EjemplarAdmin)
#admin.site.register(Biblioteca)
