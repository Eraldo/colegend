# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20141219_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag', blank=True, null=True, related_name='tasks'),
            preserve_default=True,
        ),
    ]
