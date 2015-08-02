# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0020_auto_20150802_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='max_week_streak',
            field=models.IntegerField(default=0),
        ),
    ]
