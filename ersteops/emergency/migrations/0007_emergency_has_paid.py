# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-24 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0006_auto_20180524_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='has_paid',
            field=models.BooleanField(default=False, verbose_name='Estatus de Pago'),
        ),
    ]
