# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-15 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0002_auto_20180426_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Nombre del miembro tripulante')),
                ('more_info', models.TextField(blank=True, verbose_name='Más Información acerca del miembro tripulante')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name_plural': 'Miembros de Tripulación',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='CrewRoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True, verbose_name='Tipo de integrante')),
                ('description', models.TextField(blank=True, verbose_name='Descripción del Rol')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Tripulación',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='crewmember',
            name='crewroll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_members', to='unit.CrewRoll', verbose_name='Tipo de tripulación'),
        ),
        migrations.AddField(
            model_name='unit',
            name='crew',
            field=models.ManyToManyField(blank=True, related_name='units', to='unit.CrewMember', verbose_name='Miembros de Tripulación'),
        ),
    ]
