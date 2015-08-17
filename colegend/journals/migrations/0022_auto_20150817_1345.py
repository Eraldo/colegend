# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0021_journal_max_week_streak'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='template',
            new_name='day_template',
        ),
    ]
