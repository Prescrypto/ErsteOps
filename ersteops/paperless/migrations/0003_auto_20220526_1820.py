# Generated by Django 2.2.27 on 2022-05-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0002_auto_20220519_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='service_geo_lat',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='service_geo_lon',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='airway',
            field=models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Manual', 'Manual'), ('Orofaringea', 'Orofaringea'), ('Endotraqueal', 'Endotraqueal'), ('Nasofaringea', 'Nasofaringea'), ('Ventilador', 'Ventilador'), ('Aspiracion', 'Aspiracion'), ('P.N l/min', 'P.N l/min'), ('M', 'M')], default='', max_length=20, verbose_name='Via Aerea'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='event_type',
            field=models.CharField(blank=True, choices=[('No Traumaticos', 'No Traumaticos'), ('Traumaticos', 'Traumaticos')], default='', max_length=20, verbose_name='Tipo de Evento'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='traumatics',
            field=models.CharField(blank=True, choices=[('Craneal', 'Craneal'), ('Craneoencefalico', 'Craneoencefalico'), ('Facial', 'Facial'), ('Cuello', 'Cuello'), ('Tórax', 'Tórax'), ('Abdomen', 'Abdomen'), ('Extremidades', 'Extremidades'), ('Columna vertebral', 'Columna vertebral'), ('Genitales', 'Genitales'), ('Otros', 'Otros')], default='', max_length=20, verbose_name='Traumatico'),
        ),
    ]
