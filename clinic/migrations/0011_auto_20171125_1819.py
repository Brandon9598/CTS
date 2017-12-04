# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_auto_20171125_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], default=0, max_length=3),
        ),
    ]
