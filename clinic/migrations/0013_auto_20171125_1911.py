# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_auto_20171125_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='photo_ID',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]