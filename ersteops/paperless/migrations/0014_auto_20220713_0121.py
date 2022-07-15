# Generated by Django 2.2.27 on 2022-07-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0013_medicalreport_other_pathological_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='copago_amount',
            field=models.CharField(blank=True, default='0', max_length=1, verbose_name='Co-pago'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='is_patient_unknow',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Es paciente desconocido'),
        ),
    ]