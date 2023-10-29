# Generated by Django 4.2.6 on 2023-10-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Carrera', models.CharField(max_length=100)),
                ('Correo_electronico', models.EmailField(max_length=254)),
                ('Usuario', models.CharField(max_length=25)),
                ('Contraseña', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
            },
        ),
    ]
