# Generated by Django 2.2.27 on 2022-10-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperless', '0036_auto_20220928_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalreport',
            name='email_sent',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
