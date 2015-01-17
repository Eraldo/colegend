# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20141211_1935'),
        ('journals', '0017_auto_20150117_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='journal_entry_template',
        ),
    ]
