# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0015_auto_20150129_0411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='walk',
            options={'ordering': ['-start']},
        ),
    ]
