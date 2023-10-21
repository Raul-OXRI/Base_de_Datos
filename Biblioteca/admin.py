from django.contrib import admin
from .models import Biblioteca,Encargado

def get_encargado(obj):
    return ', '.join([encargado.Nombre for encargado in obj.Encargado.all()])

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Ubicacion', 'Region', get_encargado)
    #readonly_fields=('Created' , 'Updated')

admin.site.register(Encargado)
admin.site.register(Biblioteca,BibliotecaAdmin)
