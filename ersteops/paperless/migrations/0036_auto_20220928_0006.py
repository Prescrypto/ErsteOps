# Generated by Django 2.2.27 on 2022-09-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0035_auto_20220824_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='patient_phone',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Telefono:'),
        ),
    ]
