# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 13:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Internal', '0005_employeeprofile_department'),
        ('Devices', '0007_auto_20180119_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceAssingment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.date.today)),
                ('release_date', models.DateField(default=None)),
                ('assign_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_devices', to=settings.AUTH_USER_MODEL)),
                ('possess_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='possessed_devices', to=settings.AUTH_USER_MODEL)),
                ('possess_place', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='possessed_devices', to='Internal.Places')),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='assign_to',
        ),
        migrations.RemoveField(
            model_name='device',
            name='possess_by',
        ),
        migrations.RemoveField(
            model_name='device',
            name='possess_place',
        ),
        migrations.AddField(
            model_name='device',
            name='assigned',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Devices.DeviceAssingment'),
        ),
    ]
