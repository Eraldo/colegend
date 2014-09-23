# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'priority', 'project', 'name']},
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=2),
        ),
    ]
