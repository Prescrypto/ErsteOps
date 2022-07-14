# Generated by Django 2.2.27 on 2022-07-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0019_auto_20220713_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='inmovilization',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Inmovilizacion'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='inmovilization_type',
            field=models.CharField(blank=True, choices=[('Columna Cervical', 'Columna Cervical'), ('Columna Toracica', 'Columna Toracica'), ('Extremidades', 'Extremidades'), ('Total', 'Total'), ('Otro', 'Otro')], default='', max_length=150, verbose_name='Inmovilizacion'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='pupil_state_left',
            field=models.CharField(blank=True, choices=[('Isocoria', 'Isocoria'), ('Midriasis', 'Midriasis'), ('Miosis', 'Miosis'), ('Anisocoria', 'Anisocoria')], default='', max_length=150, verbose_name='Estado de la pupila, Izquierda'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='pupil_state_right',
            field=models.CharField(blank=True, choices=[('Isocoria', 'Isocoria'), ('Midriasis', 'Midriasis'), ('Miosis', 'Miosis'), ('Anisocoria', 'Anisocoria')], default='', max_length=150, verbose_name='Estado de la pupilas, Derecha'),
        ),
    ]
