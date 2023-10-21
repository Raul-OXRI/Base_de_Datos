from django.contrib import admin
from Biblioteca.models import Biblioteca
from .models import Ejemplar
# Register your models here.

def get_biblioteca(obj):
    return ', '.join([biblioteca.Nombre for biblioteca in obj.Biblioteca.all()])

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Tipo', 'Existencia', get_biblioteca)


admin.site.register(Ejemplar, EjemplarAdmin)
#admin.site.register(Biblioteca)
