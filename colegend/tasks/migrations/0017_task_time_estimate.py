# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_auto_20150802_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_estimate',
            field=models.DurationField(blank=True, null=True, help_text='DD HH:MM:SS'),
        ),
    ]
