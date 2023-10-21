from django.contrib import admin
from .models import Biblioteca,Encargado


class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Ubicacion', 'Region', 'Encargado')
    #readonly_fields=('Created' , 'Updated')

admin.site.register(Encargado)
admin.site.register(Biblioteca,BibliotecaAdmin)
