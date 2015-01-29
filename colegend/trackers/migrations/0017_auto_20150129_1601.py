# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0016_auto_20150129_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dream',
            options={'ordering': ['-date']},
        ),
    ]
