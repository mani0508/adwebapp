# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0005_auto_20160208_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
