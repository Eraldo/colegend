# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150414_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projects', to='tags.Tag'),
        ),
    ]
