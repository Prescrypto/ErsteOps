# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-24 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0005_auto_20180524_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='erste_code',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='ID Code'),
        ),
        migrations.AlterField(
            model_name='emergency',
            name='odoo_client',
            field=models.CharField(max_length=50, verbose_name='Cliente id(Legacy)'),
        ),
    ]
