# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0009_auto_20180119_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceassingment',
            name='release_date',
        ),
        migrations.AlterField(
            model_name='deviceassingment',
            name='device',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='Devices.Device'),
        ),
    ]
