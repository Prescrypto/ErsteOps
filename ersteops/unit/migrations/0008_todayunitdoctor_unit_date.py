# Generated by Django 2.2.27 on 2022-06-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0007_todayunitdoctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='todayunitdoctor',
            name='unit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Dia/Hora'),
        ),
    ]
