# Generated by Django 2.2.27 on 2022-06-03 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0005_medicalreport_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
    ]
