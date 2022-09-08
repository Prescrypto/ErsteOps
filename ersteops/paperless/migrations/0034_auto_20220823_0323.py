# Generated by Django 2.2.27 on 2022-08-23 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0033_medicalreport_odoo_client_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalreport',
            name='odoo_client_data',
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='odoo_client_name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Socio'),
        ),
    ]
