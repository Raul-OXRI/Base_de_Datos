# Generated by Django 4.2.6 on 2023-10-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0002_remove_reserva_cantidad_dias'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Cantidad_dias',
            field=models.SmallIntegerField(default=10, verbose_name='Cantidad de Dias a Reservar'),
        ),
    ]
