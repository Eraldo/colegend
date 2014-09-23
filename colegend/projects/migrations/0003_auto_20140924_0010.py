# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['status', 'priority', 'name']},
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=2),
        ),
    ]
