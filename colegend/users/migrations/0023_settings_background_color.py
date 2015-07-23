# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_settings_journal_entry_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='background_color',
            field=colorful.fields.RGBColorField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
