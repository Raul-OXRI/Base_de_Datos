# Generated by Django 4.2.6 on 2023-10-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id_encargado', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Telefono', models.CharField(default='+502 ', help_text='El número de teléfono debe tener 8 dígitos,sin espacios.', max_length=13)),
                ('Correo_electronico', models.EmailField(max_length=254)),
                ('Contrasena', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'encargado',
                'verbose_name_plural': 'encargados',
            },
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Ubicacion', models.CharField(max_length=50)),
                ('Region', models.CharField(choices=[('metropolitana', 'Metropolitana'), ('norte', 'Norte'), ('sur-occidente', 'Sur-occidente'), ('sur-oriente', 'sur-oriente'), ('nor-oriente', 'Nor-oriente'), ('nor-occidente', 'Nor-occidente'), ('central', 'Central')], max_length=13)),
                ('Horario', models.CharField(max_length=50)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now_add=True)),
                ('Encargado', models.ManyToManyField(blank=True, to='Biblioteca.encargado')),
            ],
            options={
                'verbose_name': 'biblioteca',
                'verbose_name_plural': 'bibliotecas',
            },
        ),
    ]
