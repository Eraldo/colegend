# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_user_date_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='journal_entry_template',
            field=models.TextField(default='', help_text='The default text to be used as a basis when creating a new journal entry.', blank=True),
            preserve_default=False,
        ),
    ]
