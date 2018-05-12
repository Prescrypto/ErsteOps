# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-27 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decisiontree', '0002_symptomdatadetail_symptomdatafile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='symptomdatadetail',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Symptom Data Detail'},
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='level',
            field=models.CharField(default='', max_length=2, verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n1',
            field=models.CharField(default='', max_length=3, verbose_name='N1'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n2',
            field=models.CharField(default='', max_length=3, verbose_name='N2'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n3',
            field=models.CharField(default='', max_length=3, verbose_name='N3'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n4',
            field=models.CharField(default='', max_length=3, verbose_name='N4'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n5',
            field=models.CharField(default='', max_length=3, verbose_name='N5'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n6',
            field=models.CharField(default='', max_length=3, verbose_name='N6'),
        ),
        migrations.AlterField(
            model_name='symptomdatadetail',
            name='n7',
            field=models.CharField(default='', max_length=3, verbose_name='N7'),
        ),
    ]