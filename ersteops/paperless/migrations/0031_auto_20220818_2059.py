# Generated by Django 2.2.27 on 2022-08-18 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0030_medicalreport_final_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='signature_client',
            field=models.TextField(blank=True, verbose_name='Signature Client'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='final_report',
            field=models.FileField(blank=True, default='', upload_to='pdffile/pdf_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])], verbose_name='archivo de estudios(pdf o jpg)'),
        ),
    ]