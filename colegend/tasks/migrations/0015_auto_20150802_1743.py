# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20150414_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='tags.Tag'),
        ),
    ]
