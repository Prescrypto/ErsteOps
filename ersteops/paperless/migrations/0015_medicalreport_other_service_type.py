# Generated by Django 2.2.27 on 2022-07-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0014_auto_20220713_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='other_service_type',
            field=models.CharField(blank=True, default='', max_length=9, verbose_name='Tipo de Servicio'),
        ),
    ]
