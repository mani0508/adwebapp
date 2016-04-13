# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_lighteningtype_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lighteningtype',
            name='choice',
        ),
    ]
