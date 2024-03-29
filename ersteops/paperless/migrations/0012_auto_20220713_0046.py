# Generated by Django 2.2.27 on 2022-07-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0011_auto_20220607_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalExploration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='Dia/Hora')),
                ('heart_rate', models.CharField(blank=True, default='', max_length=20, verbose_name='Frequencia Cardiaca')),
                ('respiratory_rate', models.CharField(blank=True, default='', max_length=20, verbose_name='Frequencia Respiratoria')),
                ('blood_pressure', models.CharField(blank=True, default='', max_length=20, verbose_name='Presion Arterial')),
                ('temperature', models.CharField(blank=True, default='', max_length=20, verbose_name='Temperature')),
                ('oxygen_saturation', models.CharField(blank=True, default='', max_length=20, verbose_name='Saturacion O2')),
                ('glucometry', models.CharField(blank=True, default='', max_length=20, verbose_name='Glucometria')),
                ('glassgow_motor', models.CharField(blank=True, default='', max_length=20, verbose_name='Glassgow Motor')),
                ('glassgow_verbal', models.CharField(blank=True, default='', max_length=20, verbose_name='Glassgow Verbal')),
                ('glassgow_ocular', models.CharField(blank=True, default='', max_length=20, verbose_name='Glassgow Ocular')),
                ('glassgow_final', models.CharField(blank=True, default='', max_length=20, verbose_name='Glassgow Final')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name_plural': 'Exploracion Fisica',
                'ordering': ['created_at'],
            },
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_blood_pressure',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_glassgow',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_glucometry',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_heart_rate',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_oxygen_saturation',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_respiratory_rate',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_temperature',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pe_time',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='pupil_state',
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='inmovilization',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Inmovilizacion'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='inmovilization_type',
            field=models.CharField(blank=True, choices=[('Columna Cervical', 'Columna Cervical'), ('Columna Toracica', 'Columna Toracica'), ('Extremidades', 'Extremidades'), ('Total', 'Total'), ('Otro', 'Otro')], default='', max_length=50, verbose_name='Inmovilizacion'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='other_airway',
            field=models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Manual', 'Manual'), ('Orofaringea', 'Orofaringea'), ('Endotraqueal', 'Endotraqueal'), ('Nasofaringea', 'Nasofaringea'), ('Ventilador', 'Ventilador'), ('Aspiracion', 'Aspiracion'), ('P.N l/min', 'P.N l/min'), ('M', 'M')], default='', max_length=20, verbose_name='Otra Via Aerea'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='other_attention_place',
            field=models.CharField(blank=True, choices=[('Hogar', 'Hogar'), ('Escuela/Trabajo', 'Escuela/Trabajo'), ('Ins.deportivas', 'Ins.deportivas'), ('Ins. de recreacion', 'Ins. de recreacion'), ('Via Publica', 'Via Publica'), ('Otro', 'Otro')], default='', max_length=20, verbose_name='Otro Sitio de Atencion'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='other_consultation_reason',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Otro Motivo de la Consulta'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='other_inmovilization_type',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Otra Inmovilizacion'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='other_traumatics',
            field=models.CharField(blank=True, choices=[('Craneal', 'Craneal'), ('Craneoencefalico', 'Craneoencefalico'), ('Facial', 'Facial'), ('Cuello', 'Cuello'), ('Tórax', 'Tórax'), ('Abdomen', 'Abdomen'), ('Extremidades', 'Extremidades'), ('Columna vertebral', 'Columna vertebral'), ('Genitales', 'Genitales'), ('Otros', 'Otros')], default='', max_length=50, verbose_name='Otro Traumatico'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='patient_address',
            field=models.CharField(default='', max_length=50, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='pupil_state_left',
            field=models.CharField(blank=True, choices=[('Isocoria', 'Isocoria'), ('Midriasis', 'Midriasis'), ('Miosis', 'Miosis'), ('Anisocoria', 'Anisocoria')], default='', max_length=50, verbose_name='Estado de la pupila, Izquierda'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='pupil_state_right',
            field=models.CharField(blank=True, choices=[('Isocoria', 'Isocoria'), ('Midriasis', 'Midriasis'), ('Miosis', 'Miosis'), ('Anisocoria', 'Anisocoria')], default='', max_length=50, verbose_name='Estado de la pupilas, Derecha'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='service_crum',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Folio CRUM'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='service_crum_dr',
            field=models.CharField(blank=True, default='', max_length=60, verbose_name='Medico CRUM'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='attention_place',
            field=models.CharField(blank=True, choices=[('Hogar', 'Hogar'), ('Escuela/Trabajo', 'Escuela/Trabajo'), ('Ins.deportivas', 'Ins.deportivas'), ('Ins. de recreacion', 'Ins. de recreacion'), ('Via Publica', 'Via Publica'), ('Otro', 'Otro')], default='', max_length=20, verbose_name='Sitio de Atencion'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='traumatics',
            field=models.CharField(blank=True, choices=[('Craneal', 'Craneal'), ('Craneoencefalico', 'Craneoencefalico'), ('Facial', 'Facial'), ('Cuello', 'Cuello'), ('Tórax', 'Tórax'), ('Abdomen', 'Abdomen'), ('Extremidades', 'Extremidades'), ('Columna vertebral', 'Columna vertebral'), ('Genitales', 'Genitales'), ('Otros', 'Otros')], default='', max_length=100, verbose_name='Traumatico'),
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='physical_exploration',
            field=models.ManyToManyField(blank=True, related_name='physical_exploration', to='paperless.PhysicalExploration'),
        ),
    ]
