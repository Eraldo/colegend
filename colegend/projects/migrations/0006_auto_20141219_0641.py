# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20141116_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['status', 'name']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='priority',
        ),
    ]
