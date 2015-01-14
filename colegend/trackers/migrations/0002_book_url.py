# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
    ]
