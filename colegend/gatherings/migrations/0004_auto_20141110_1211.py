# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0003_auto_20141104_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='location',
            field=models.CharField(max_length=200, default='http://gathering.colegend.org/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gathering',
            name='online',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
