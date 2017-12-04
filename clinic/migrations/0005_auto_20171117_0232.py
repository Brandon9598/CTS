# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-17 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20171110_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(default='A+', max_length=2),
        ),
        migrations.AddField(
            model_name='patient',
            name='language',
            field=models.CharField(default='blank', max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='national_id',
            field=models.CharField(default='0000000000', max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_num',
            field=models.IntegerField(default='18005000000', max_length=11),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='blank', max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='blank', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='blank', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(default='0000000000', max_length=30),
        ),
    ]