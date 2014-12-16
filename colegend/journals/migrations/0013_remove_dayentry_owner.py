# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0012_auto_20141216_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayentry',
            name='owner',
        ),
    ]
