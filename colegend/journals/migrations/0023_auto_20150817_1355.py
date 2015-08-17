# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0022_auto_20150817_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='week_template',
            field=models.TextField(blank=True, help_text='The default text to be used as a basis when creating a new journal week entry.'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='day_template',
            field=models.TextField(blank=True, help_text='The default text to be used as a basis when creating a new journal day entry.'),
        ),
    ]
