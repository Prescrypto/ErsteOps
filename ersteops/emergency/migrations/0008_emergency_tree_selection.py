# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-04 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0007_emergency_has_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='tree_selection',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Internal Code for tree selection'),
        ),
    ]