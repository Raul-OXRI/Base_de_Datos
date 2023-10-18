# Generated by Django 4.2.6 on 2023-10-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Ubicacion', models.CharField(max_length=50)),
                ('Encargado', models.CharField(max_length=50)),
                ('Horario', models.CharField(max_length=50)),
                ('Numero_libros', models.IntegerField(default=200)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]
