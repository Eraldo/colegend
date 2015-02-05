# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0018_auto_20150204_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='chart_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Calendar Chart'), (1, 'Column Chart'), (2, 'Line Chart')], default=0),
            preserve_default=True,
        ),
    ]
