# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hoarding',
            fields=[
                ('hoarding_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('category', models.ForeignKey(to='codes.Category')),
            ],
        ),
        migrations.CreateModel(
            name='LighteningType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='hoarding',
            name='hoarding_type',
            field=models.ForeignKey(to='codes.OutdoorType'),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='lightening',
            field=models.ForeignKey(to='codes.LighteningType'),
        ),
    ]
