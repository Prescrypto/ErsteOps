# Generated by Django 2.2.27 on 2022-07-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0025_auto_20220714_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='other_service_type',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Tipo de Servicio'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='service_type',
            field=models.CharField(blank=True, choices=[('Traslado', 'Traslado'), ('Urgencias', 'Urgencias'), ('Cuidados Intensivos', 'Cuidados Intensivos'), ('Consulta Medica', 'Consulta Medica')], default='', max_length=50, verbose_name='Tipo de Servicio'),
        ),
    ]
