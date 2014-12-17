# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0013_remove_dayentry_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='max_streak',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
