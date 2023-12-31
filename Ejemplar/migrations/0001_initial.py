# Generated by Django 4.2.6 on 2023-10-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.ImageField(upload_to='')),
                ('Titulo', models.CharField(max_length=100)),
                ('Autor', models.CharField(max_length=100)),
                ('Año', models.IntegerField()),
                ('Editorial', models.CharField(max_length=100)),
                ('Tipo', models.CharField(choices=[('papel', 'Papel'), ('electronico', 'Electronico'), ('interactivo', 'Interactivo')], max_length=11)),
                ('Existencia', models.IntegerField()),
                ('Biblioteca', models.ManyToManyField(blank=True, to='Biblioteca.biblioteca')),
            ],
            options={
                'verbose_name': 'ejemplar',
                'verbose_name_plural': 'ejemplar',
            },
        ),
    ]
