# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0013_auto_20171213_0634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='symptom2',
            options={'ordering': ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7']},
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n1',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n2',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n3',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n4',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n5',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n6',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='n7',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='symptom2',
            name='nivel',
            field=models.CharField(blank=True, default='0', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='symptom2',
            name='grado',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
