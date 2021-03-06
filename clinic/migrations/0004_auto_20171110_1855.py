# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20171110_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='visits',
        ),
        migrations.AddField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinic.Patient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Doctor'),
        ),
    ]
