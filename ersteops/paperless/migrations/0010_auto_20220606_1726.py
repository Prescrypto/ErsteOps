# Generated by Django 2.2.27 on 2022-06-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0009_auto_20220606_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='erste_code',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='ID Code'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='odoo_client',
            field=models.CharField(default='', max_length=50, verbose_name='Cliente id(Legacy)'),
        ),
    ]
