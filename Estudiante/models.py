from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Carrera = models.CharField(max_length=100)
    Correo_electronico = models.EmailField()
    Usuario = models.CharField(max_length=25)
    Contraseña = models.CharField(max_length=25)

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return f"{self.usuario} {self.Correo_electronico}"