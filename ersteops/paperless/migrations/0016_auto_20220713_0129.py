# Generated by Django 2.2.27 on 2022-07-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0015_medicalreport_other_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='crum',
            field=models.CharField(blank=True, default=False, max_length=20, verbose_name='Folio CRUM'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='crum_reception',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default=False, max_length=120, verbose_name='Medico Recibe CRUM'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='demarcation',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default=False, max_length=20, verbose_name='Deslinde'),
        ),
    ]
