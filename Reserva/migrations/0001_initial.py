# Generated by Django 4.2.6 on 2023-10-29 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ejemplar', '0001_initial'),
        ('Estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad_dias', models.IntegerField(default=10, verbose_name='Cantida de dias a reservar')),
                ('Fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('Fecha_vencida', models.DateField(auto_now_add=True, verbose_name='Fecha de vencimiento de reserva')),
                ('Estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('Ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejemplar.ejemplar')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estudiante.estudiante')),
            ],
            options={
                'verbose_name': 'reserva',
                'verbose_name_plural': 'reservas',
            },
        ),
    ]
