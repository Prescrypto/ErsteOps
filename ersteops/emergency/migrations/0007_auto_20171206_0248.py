# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0006_auto_20171206_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttentionDerivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.CharField(blank=True, max_length=100, verbose_name='Motivo')),
                ('eventualities', models.TextField(blank=True, max_length=100, verbose_name='eventualidades')),
                ('reception', models.CharField(blank=True, max_length=100, verbose_name='quien recibe en hospital')),
                ('notes', models.TextField(blank=True, max_length=100, verbose_name='notas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='ultima modificacion')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'Derivacion',
            },
        ),
        migrations.CreateModel(
            name='AttentionHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='hospital')),
                ('address', models.TextField(blank=True, max_length=100, verbose_name='direccion')),
                ('phone', models.CharField(blank=True, default='', max_length=15, verbose_name='telefono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='ultima modificacion')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Hospital',
            },
        ),
        migrations.RemoveField(
            model_name='emergency',
            name='patient_age',
        ),
        migrations.RemoveField(
            model_name='emergency',
            name='patient_gender',
        ),
        migrations.AddField(
            model_name='attentionderivation',
            name='emergency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='derivation_emergency_name', to='emergency.Emergency', verbose_name='emergencia'),
        ),
        migrations.AddField(
            model_name='attentionderivation',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attention_hospital_name', to='emergency.AttentionHospital', verbose_name='hospital'),
        ),
    ]
