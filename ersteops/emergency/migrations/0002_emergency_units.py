# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
        ('emergency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='units',
            field=models.ManyToManyField(blank=True, related_name='units', to='unit.Unit'),
        ),
    ]