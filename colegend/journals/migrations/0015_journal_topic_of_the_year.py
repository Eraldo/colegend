# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0014_journal_max_streak'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='topic_of_the_year',
            field=models.CharField(max_length=100, blank=True, default=''),
            preserve_default=False,
        ),
    ]
