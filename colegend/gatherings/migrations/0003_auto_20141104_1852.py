# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0002_auto_20141001_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gathering',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
