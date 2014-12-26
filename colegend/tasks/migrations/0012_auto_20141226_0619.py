# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20141221_0301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'project', '-modification_date']},
        ),
    ]
