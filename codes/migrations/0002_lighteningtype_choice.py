# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lighteningtype',
            name='choice',
            field=models.CharField(default=datetime.datetime(2016, 2, 8, 8, 42, 29, 283790, tzinfo=utc), max_length=50, choices=[(b'Audio', ((b'vinyl', b'Vinyl'), (b'cd', b'CD'))), (b'Video', ((b'vhs', b'VHS Tape'), (b'dvd', b'DVD'))), (b'unknown', b'Unknown')]),
            preserve_default=False,
        ),
    ]
