# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decisiontree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SymptomDataDetail',
            fields=[
                ('idx', models.CharField(max_length=18, primary_key=True, serialize=False, unique=True, verbose_name='idx')),
                ('name', models.CharField(default='', max_length=200, verbose_name='sintoma')),
                ('n1', models.CharField(default='', max_length=1, verbose_name='N1')),
                ('n2', models.CharField(default='', max_length=1, verbose_name='N2')),
                ('n3', models.CharField(default='', max_length=1, verbose_name='N3')),
                ('n4', models.CharField(default='', max_length=1, verbose_name='N4')),
                ('n5', models.CharField(default='', max_length=1, verbose_name='N5')),
                ('n6', models.CharField(default='', max_length=1, verbose_name='N6')),
                ('n7', models.CharField(default='', max_length=1, verbose_name='N7')),
                ('level', models.CharField(default='', max_length=1, verbose_name='Nivel')),
                ('grade', models.CharField(default='', max_length=50, verbose_name='Grado')),
                ('key', models.CharField(default='', max_length=18, verbose_name='Clave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='ultima modificacion')),
                ('symptom_type', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='symptom_type_name', to='decisiontree.SymptomType', verbose_name='symptom_type')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'Biometric Data Detail',
            },
        ),
        migrations.CreateModel(
            name='SymptomDataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nombre de la carga')),
                ('symptom_file', models.FileField(default='', upload_to='decisiontree/symptom_files', verbose_name='archivo de syntomas')),
                ('procesed', models.NullBooleanField(verbose_name='procesado')),
                ('read_lines', models.IntegerField(blank=True, default=0, verbose_name='Lineas leida')),
                ('insert_lines', models.IntegerField(blank=True, default=0, verbose_name='Lineas Insertadas')),
                ('update_lines', models.IntegerField(blank=True, default=0, verbose_name='Lineas actualizadas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='ultima modificacion')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'Symptom Data File',
            },
        ),
    ]