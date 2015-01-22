# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0011_auto_20150121_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sleep',
            options={'ordering': ['-start']},
        ),
    ]
