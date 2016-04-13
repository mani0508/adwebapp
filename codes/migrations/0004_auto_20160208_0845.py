# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0003_remove_lighteningtype_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lighteningtype',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
