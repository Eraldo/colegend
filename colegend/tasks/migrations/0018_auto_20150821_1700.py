# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_task_time_estimate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_estimate',
            field=lib.modelfields.IntuitiveDurationField(null=True, blank=True),
        ),
    ]
