# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0015_journal_topic_of_the_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='template',
            field=models.TextField(default='', help_text='The default text to be used as a basis when creating a new journal entry.', blank=True),
            preserve_default=False,
        ),
    ]
