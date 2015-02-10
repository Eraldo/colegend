# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0019_tracker_chart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tags',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
