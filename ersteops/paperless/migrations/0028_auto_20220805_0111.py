# Generated by Django 2.2.27 on 2022-08-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0027_auto_20220804_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_abdomen',
            field=models.TextField(blank=True, verbose_name='Notas Abdomen'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_face',
            field=models.TextField(blank=True, verbose_name='Notas Cara'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_genitals',
            field=models.TextField(blank=True, verbose_name='Notas Genitales'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_head',
            field=models.TextField(blank=True, verbose_name='Notas Cabeza'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_limbs',
            field=models.TextField(blank=True, verbose_name='Notas Extremidades'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_neck',
            field=models.TextField(blank=True, verbose_name='Notas Cara'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_spine',
            field=models.TextField(blank=True, verbose_name='Notas Columna Vertebral'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='det_normal_torax',
            field=models.TextField(blank=True, verbose_name='Notas Tórax'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_alergy',
            field=models.TextField(blank=True, verbose_name='Notas Alergias'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_arterial_hypertension',
            field=models.TextField(blank=True, verbose_name='Notas Hipertension Arterial'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_daibetes_melitus',
            field=models.TextField(blank=True, verbose_name='Notas Diabetes Melitus'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_heart_disease',
            field=models.TextField(blank=True, verbose_name='Notas Cardiopatias'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_pneumopathies',
            field=models.TextField(blank=True, verbose_name='Notas Neumopatias'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='detail_pat_history_trauma',
            field=models.TextField(blank=True, verbose_name='Notas Quirurgicos/Trauma'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='normal_neck',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='', max_length=10, verbose_name='Cuello'),
        ),
    ]
