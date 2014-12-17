# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def update_completion_dates(apps, schema_editor):
        task_class = apps.get_model("tasks", "Task")
        for task in task_class.objects.all():
            if task.status.name in ('done', 'canceled'):
                task.completion_date = task.modification_date
                task.save()

    dependencies = [
        ('tasks', '0008_task_completion_date'),
    ]

    operations = [
        migrations.RunPython(update_completion_dates),
    ]
