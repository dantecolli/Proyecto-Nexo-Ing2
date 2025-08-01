# Generated by Django 5.2.1 on 2025-06-11 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_alter_solicitudreserva_estado_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarjetaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16, unique=True)),
                ('vencimiento', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='solicitudreserva',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=50),
        ),
        migrations.CreateModel(
            name='PagoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('solicitud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservas.solicitudreserva')),
            ],
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
    ]
